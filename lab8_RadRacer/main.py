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
        self.vehicle_positions = [0] * lanes  # Store previous positions

    def _create_track(self):
        track = [['-' for _ in range(self.length)] for _ in range(self.lanes)]
        for lane in track:
            obstacle_positions = random.sample(range(1, self.length - 1), 2)  # Exclude start and finish
            for pos in obstacle_positions:
                lane[pos] = '0'
        return track

    def display(self, vehicles):
        for i, vehicle in enumerate(vehicles):
            pos = min(vehicle.position, self.length - 1)
            # Add '*' for the previous position and save it on the track
            if self.vehicle_positions[i] > 0 and self.vehicle_positions[i] < self.length and self.track[i][self.vehicle_positions[i]] == '-':
                self.track[i][self.vehicle_positions[i]] = '*'
            # Place the vehicle on the track
            if pos < self.length:
                self.track[i][pos] = 'P' if vehicle.initial == 'P' else vehicle.initial
            self.vehicle_positions[i] = pos  # Update previous position
        for lane in self.track:
            print(''.join(lane))
        # Reset vehicle positions on the track to '-' or '*'
        for i, vehicle in enumerate(vehicles):
            pos = min(vehicle.position, self.length - 1)
            if pos < self.length:
                self.track[i][pos] = '*' if self.track[i][pos] != '0' else '0'

    def is_obstacle_ahead(self, lane, position):
        return self.track[lane][position] == '0'

    def clear_obstacles(self, lane, start_pos):
        for i in range(start_pos, self.length):
            if self.track[lane][i] == '0':
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
        for i in range(self.player.position + 1, self.track.length):
            if self.track.is_obstacle_ahead(player_lane, i):
                next_obstacle = i - self.player.position
                break

        if action == 1:
            result = self.player.fast(next_obstacle)
            print(result)
        elif action == 2:
            result = self.player.slow(next_obstacle)
            print(result)
        else:
            result = self.player.special_move(next_obstacle)
            print(result)
            
            # Clear obstacles if it's a truck using special move
            if isinstance(self.player, truck.Truck) and action == 3:
                self.track.clear_obstacles(player_lane, self.player.position)

        # Computer's Turn
        for opponent in self.vehicles:
            if opponent != self.player:
                opponent_lane = self.vehicles.index(opponent)
                next_obstacle = self.track.length
                for i in range(opponent.position + 1, self.track.length):
                    if self.track.is_obstacle_ahead(opponent_lane, i):
                        next_obstacle = i - opponent.position
                        break

                if random.random() < 0.2:  # 20% chance of special move
                    result = opponent.special_move(next_obstacle)
                    print(result)
                    if isinstance(opponent, truck.Truck):
                        # Clear obstacles if it's a truck using special move
                        self.track.clear_obstacles(opponent_lane, opponent.position)
                elif random.random() < 0.7:  # 70% chance of fast move
                    result = opponent.fast(next_obstacle)
                    print(result)
                else:
                    result = opponent.slow(next_obstacle)
                    print(result)

    def get_winner(self):
        return max(self.vehicles, key=lambda v: v.position)

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
    player.initial = 'P'

    track = RaceTrack()
    race = Race(player, vehicles, track)

    winner = None
    while not winner:
        print("\n" + str(c))
        print(str(m))
        print(str(t))
        track.display(vehicles)  # Display track at the beginning of each turn
        race.play_turn()
        
        # Check for a winner
        for vehicle in vehicles:
            if vehicle.position >= track.length:
                winner = vehicle
                break
    
    # Ensure all vehicles are at or past the finish line for the final display
    for vehicle in vehicles:
        if vehicle.position < track.length:
            vehicle.position = track.length
    
    track.display(vehicles)  # Display final positions
    print(f"\nThe winner is {winner._name}!")

if __name__ == "__main__":
    main()
