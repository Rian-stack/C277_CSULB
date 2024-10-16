import car
import motorcycle
import truck
import check_input
import random

class Game:
    def __init__(self):
        self.TRACK_LENGTH = 100
        self.OBSTACLE_CHANCE = 0.2
        self.LANES = 3
        self.vehicles = [
            car.Car("Lightning Car", "C", 6, 8),
            motorcycle.Motorcycle("Swift Bike", "M", 6, 8),
            truck.Truck("Behemoth Truck", "T", 4, 8)
        ]
        self.track = self.create_track()
        self.player = None

    def create_track(self):
        track = [['-' for _ in range(self.TRACK_LENGTH)] for _ in range(self.LANES)]
        for lane in track:
            obstacle_positions = random.sample(range(1, self.TRACK_LENGTH - 1), 2)  # Exclude start and finish
            for pos in obstacle_positions:
                lane[pos] = '0'
        return track

    def display_track(self):
        display_track = [lane.copy() for lane in self.track]
        for i, vehicle in enumerate(self.vehicles):
            pos = min(vehicle.get_position(), self.TRACK_LENGTH - 1)
            display_track[i][pos] = 'P' if vehicle._initial == 'P' else vehicle._initial
            # Add '*' for previous starting positions
            if pos > 0:
                display_track[i][0] = '*'
        for lane in display_track:
            print(''.join(lane))

    def choose_player(self):
        for i, vehicle in enumerate(self.vehicles, 1):
            print(f"{i}. {vehicle.description()}")
        choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)
        self.player = self.vehicles[choice - 1]
        self.player._initial = 'P'

    def player_turn(self):
        action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        player_lane = self.vehicles.index(self.player)
        next_obstacle = next((i for i in range(self.player.get_position() + 1, self.TRACK_LENGTH) if self.track[player_lane][i] == '0'), self.TRACK_LENGTH)
        distance_to_obstacle = next_obstacle - self.player.get_position()

        if action == 1:
            result = self.player.fast(distance_to_obstacle)
        elif action == 2:
            result = self.player.slow(distance_to_obstacle)
        else:
            if isinstance(self.player, truck.Truck):
                distance, smash = self.player.special_move()
                if smash:
                    for i in range(self.player.get_position(), min(self.player.get_position() + distance, self.TRACK_LENGTH)):
                        self.track[player_lane][i] = '-'
            else:
                distance = self.player.special_move()
            result = f"({self.player._name}) uses special move and travels {distance} units!"

        print(result)

    def ai_turns(self):
        for opponent in self.vehicles:
            if opponent != self.player:
                opponent_lane = self.vehicles.index(opponent)
                next_obstacle = next((i for i in range(opponent.get_position() + 1, self.TRACK_LENGTH) if self.track[opponent_lane][i] == '0'), self.TRACK_LENGTH)
                distance_to_obstacle = next_obstacle - opponent.get_position()

                if random.random() < 0.2:  # 20% chance of special move
                    if isinstance(opponent, truck.Truck):
                        distance, smash = opponent.special_move()
                        if smash:
                            for i in range(opponent.get_position(), min(opponent.get_position() + distance, self.TRACK_LENGTH)):
                                self.track[opponent_lane][i] = '-'
                    else:
                        distance = opponent.special_move()
                elif random.random() < 0.7:  # 70% chance of fast move
                    opponent.fast(distance_to_obstacle)
                else:
                    opponent.slow(distance_to_obstacle)

    def play(self):
        print("Rad Racer!")
        print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
        
        self.choose_player()

        while all(v.get_position() < self.TRACK_LENGTH for v in self.vehicles):
            print("\n" + "\n".join(str(v) for v in self.vehicles))
            self.display_track()
            self.player_turn()
            self.ai_turns()

        winner = max(self.vehicles, key=lambda v: v.get_position())
        print(f"\nThe winner is {winner._name}!")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
