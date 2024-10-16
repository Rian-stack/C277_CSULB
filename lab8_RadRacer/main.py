from car import Car
from motorcycle import Motorcycle
from truck import Truck
import check_input
import random

TRACK_LENGTH = 100
OBSTACLE_CHANCE = 0.2
LANES = 3

def create_track():
    return [['0' if random.random() < OBSTACLE_CHANCE else '-' for _ in range(TRACK_LENGTH)] for _ in range(LANES)]

def display_track(track, vehicles):
    display_track = [lane.copy() for lane in track]
    for i, vehicle in enumerate(vehicles):
        pos = min(vehicle.get_position(), TRACK_LENGTH - 1)
        display_track[i][pos] = 'P' if vehicle._initial == 'P' else vehicle._initial
    for lane in display_track:
        print(''.join(lane))

def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)

    car = Car("Lightning Car", "C", 6, 8)
    motorcycle = Motorcycle("Swift Bike", "M", 6, 8)
    truck = Truck("Behemoth Truck", "T", 4, 8)

    vehicles = [car, motorcycle, truck]
    player = vehicles[choice - 1]
    player._initial = 'P'

    track = create_track()

    while all(v.get_position() < TRACK_LENGTH for v in vehicles):
        print("\n" + str(car))
        print(str(motorcycle))
        print(str(truck))
        display_track(track, vehicles)

        # Player's turn
        action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        if action == 1:
            distance = player.fast()
        elif action == 2:
            distance = player.slow()
        else:
            if isinstance(player, Truck):
                distance, smash = player.special_move()
                if smash:
                    for i in range(player.get_position(), min(player.get_position() + distance, TRACK_LENGTH)):
                        track[vehicles.index(player)][i] = '-'
            else:
                distance = player.special_move()

        player_lane = vehicles.index(player)
        if track[player_lane][min(player.get_position() + distance, TRACK_LENGTH - 1)] == '0' and action != 2:
            print("You crashed into an obstacle!")
            player._position -= distance // 2

        # AI turns
        for ai in vehicles:
            if ai != player:
                if random.random() < 0.2:  # 20% chance of special move
                    if isinstance(ai, Truck):
                        distance, smash = ai.special_move()
                        if smash:
                            ai_lane = vehicles.index(ai)
                            for i in range(ai.get_position(), min(ai.get_position() + distance, TRACK_LENGTH)):
                                track[ai_lane][i] = '-'
                    else:
                        distance = ai.special_move()
                elif random.random() < 0.7:  # 70% chance of fast move
                    distance = ai.fast()
                else:
                    distance = ai.slow()

                ai_lane = vehicles.index(ai)
                if track[ai_lane][min(ai.get_position() + distance, TRACK_LENGTH - 1)] == '0' and not isinstance(ai, Truck):
                    ai._position -= distance // 2

    winner = max(vehicles, key=lambda v: v.get_position())
    print(f"\nThe winner is {winner._name}!")

if __name__ == "__main__":
    main()
