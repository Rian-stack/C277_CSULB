import car
import motorcycle
import truck
import check_input
import random

class RaceTrack:
    def __init__(self, length=100, lanes=3, obstacle_chance=0.2):
        self.length = length
        self.lanes = lanes
        self.obstacle_chance = obstacle_chance
        self.track = self._create_track()

    def _create_track(self):
        track = [['-' for _ in range(self.length)] for _ in range(self.lanes)]
        for lane in track:
            obstacle_positions = random.sample(range(1, self.length - 1), 2)  # Exclude start and finish
            for pos in obstacle_positions:
                lane[pos] = '0'
        return track

    def display(self, vehicles):
        display_track = [lane.copy() for lane in self.track]
        for i, vehicle in enumerate(vehicles):
            pos = min(vehicle.get_position(), self.length - 1)
            display_track[i][pos] = 'P' if vehicle.get_initial() == 'P' else vehicle.get_initial()
            # Add '*' for previous starting positions
            if pos > 0:
                display_track[i][0] = '*'
        for lane in display_track:
            print(''.join(lane))

    def is_obstacle_ahead(self, lane, position):
        return self.track[lane][position] == '0'

    def clear_obstacles(self, lane, start_pos, end_pos):
        for i in range(start_pos, min(end_pos, self.length)):
            self.track[lane][i] = '-'

class Race:
    def __init__(self, player_vehicle, vehicles, track):
        self.player = player_vehicle
        self.vehicles = vehicles
        self.track = track

    def play_turn(self):
        # Player's turn
        action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        player_lane = self.vehicles.index(self.player)
        next_obstacle = self.track.length
        for i in range(self.player.get_position() + 1, self.track.length):
            if self.track.is_obstacle_ahead(player_lane, i):
                next_obstacle = i - self.player.get_position()
                break

        if action == 1:
            result = self.player.fast(next_obstacle)
        elif action == 2:
            result = self.player.slow(next_obstacle)
        else:
            result = self.player.special_move(next_obstacle)

        print(result)

        # Computer's Turn
        for opponent in self.vehicles:
            if opponent != self.player:
                if random.random() < 0.2:  # 20% chance of special move
                    result = opponent.special_move(None)
                elif random.random() < 0.7:  # 70% chance of fast move
                    result = opponent.fast(None)
                else:
                    result = opponent.slow(None)
                print(result)

    def get_winner(self):
        return max(self.vehicles, key=lambda v: v.get_position())

def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)

    # Instantiate vehicles without parameters
    c = car.Car()
    m = motorcycle.Motorcycle()
    t = truck.Truck()

    vehicles = [c, m, t]
    player = vehicles[choice - 1]
    player.set_initial('P')

    track = RaceTrack()
    race = Race(player, vehicles, track)

    while all(v.get_position() < track.length for v in vehicles):
        print("\n" + str(c))
        print(str(m))
        print(str(t))
        track.display(vehicles)
        race.play_turn()

    winner = race.get_winner()
    print(f"\nThe winner is {winner.get_name()}!")

if __name__ == "__main__":
    main()
