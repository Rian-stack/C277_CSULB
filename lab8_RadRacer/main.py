import car
import motorcycle
import truck
import check_input
import random

""" Rad Racer Game

Written by: Sena Matsuzoe, Rianne Papa
Date: 10/16/2024

This program is a racing game where the user may pick between three different vehicles: car, motorcycle, or truck. 
Each vehicle has the option to go fast, slow, or use its special move. They have unique speeds and abilities.
There will be three tracks for each vehicle, each with two obstacles in the path. 
If the vehicle is going fast, then it may crash into it, if they are going slow, then it can go around
the obstacle. The special moves are “Nitro Boost” for the car, which makes the car go 1.5x
faster, “Wheelie” for the motorcycle, which makes it go 2x faster, but has a chance of crashing,
and “Ram” for the truck, which makes it go 2x faster and also allows it to bash through an
obstacle. Whichever vehicle reaches the finish first wins the race.

"""

class RaceTrack:
    def __init__(self, length=100, lanes=3, obstacle_chance=0.2):
        self.length = length
        self.lanes = lanes
        self.obstacle_chance = obstacle_chance
        self.track = self._create_track()

    def _create_track(self):
        track = [['-' for _ in range(self.length)] for _ in range(self.lanes)]
        for lane in track:
            for i in range(self.length):
                if random.random() < self.obstacle_chance:
                    lane[i] = '0'
        return track

    def display(self, vehicles):
        display_track = [lane[:] for lane in self.track]
        for i, vehicle in enumerate(vehicles):
            pos = min(vehicle.position, self.length - 1)
            display_track[i][pos] = vehicle.initial
        for lane in display_track:
            print(''.join(lane))

    def is_obstacle_ahead(self, lane, position):
        return self.track[lane][position] == '0'

    def clear_obstacles(self, lane, start_pos):
        for i in range(start_pos, self.length):
            if self.track[lane][i] == '0':
                self.track[lane][i] = '-'

class Race:
    """
    Represents a race in the game.

    Attributes:
        player (Vehicle): The player's vehicle.
        vehicles (list): A list of all vehicles in the race.
        track (RaceTrack): The race track.
    """

    def __init__(self, player_vehicle, vehicles, track):
        """
        Initialize a new Race instance.

        Args:
            player_vehicle (Vehicle): The player's vehicle.
            vehicles (list): A list of all vehicles in the race.
            track (RaceTrack): The race track.
        """
        self.player = player_vehicle
        self.vehicles = vehicles
        self.track = track

    def play_turn(self):
        """
        Play a single turn of the race, including the player's turn and the computer-controlled vehicles' turns.
        """
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

        # Computer's Turn
        for opponent in self.vehicles:
            if opponent != self.player:
                opponent_lane = self.vehicles.index(opponent)
                next_obstacle = self.track.length
                for i in range(opponent.position + 1, self.track.length):
                    if self.track.is_obstacle_ahead(opponent_lane, i):
                        next_obstacle = i - opponent.position
                        break

                move_choice = random.random()
                if opponent.energy < 5 or move_choice < 0.4:  # 40% chance to go slow or if out of energy
                    result = opponent.slow(next_obstacle)
                elif move_choice < 0.7:  # 30% chance to go fast
                    result = opponent.fast(next_obstacle)
                else:  # 30% chance to do special move
                    result = opponent.special_move(next_obstacle)
                print(result)

    def get_winner(self):
        """
        Determine the winner of the race.

        Returns:
            Vehicle: The vehicle that has progressed the furthest on the track.
        """
        return max(self.vehicles, key=lambda v: v.position)

def main():
    """
    The main function to run the Rad Racer game.
    """
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

    # Create the race track and start the race
    track = RaceTrack()
    race = Race(player, vehicles, track)

    # Main game loop
    race_finished = False
    while not race_finished:
        track.display(vehicles)
        print("\nCurrent standings:")
        for v in vehicles:
            print(v)
        
        if all(v.position >= track.length for v in vehicles):
            race_finished = True
        else:
            race.play_turn()
            print("\n" + "="*50 + "\n")

    # Display final results
    winner = race.get_winner()
    print(f"\nThe winner is {winner._name}!")
main()
