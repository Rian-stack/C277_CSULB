import car
import motorcycle
import truck
import check_input
import random

TRACK_LENGTH = 100
OBSTACLE_CHANCE = 0.2
LANES = 3

def create_track():
    track = [['-' for _ in range(TRACK_LENGTH)] for _ in range(LANES)]
    for lane in track:
        obstacle_positions = random.sample(range(1, TRACK_LENGTH - 1), 2)  # Exclude start and finish
        for pos in obstacle_positions:
            lane[pos] = '0'
    return track

def display_track(track, vehicles):
    display_track = [lane.copy() for lane in track]
    for i, vehicle in enumerate(vehicles):
        pos = min(vehicle.get_position(), TRACK_LENGTH - 1)
        display_track[i][pos] = 'P' if vehicle._initial == 'P' else vehicle._initial
        # Add '*' for previous starting positions
        if pos > 0:
            display_track[i][0] = '*'
    for lane in display_track:
        print(''.join(lane))

def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning car.Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)

    c = car.Car("Lightning car.Car", "C", 6, 8)
    m = motorcycle.Motorcycle("Swift Bike", "M", 6, 8)
    t = truck.Truck("Behemoth Truck", "T", 4, 8)

    vehicles = [c, m, t]
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
        player_lane = vehicles.index(player)
        next_obstacle = TRACK_LENGTH
        for i in range(player.get_position() + 1, TRACK_LENGTH):
            if track[player_lane][i] == '0':
                next_obstacle = i - player.get_position()
                break

        if action == 1:
            result = player.fast(next_obstacle)
        elif action == 2:
            result = player.slow(next_obstacle)
        else:
            if isinstance(player, Truck):
                distance, smash = player.special_move()
                if smash:
                    for i in range(player.get_position(), min(player.get_position() + distance, TRACK_LENGTH)):
                        track[player_lane][i] = '-'
                result = f"({player._name}) uses special move and travels {distance} units!"
            else:
                distance = player.special_move()
                result = f"({player._name}) uses special move and travels {distance} units!"

        print(result)

        # AI turns
        for opponent in vehicles:
            if opponent != player:
                if random.random() < 0.2:  # 20% chance of special move
                    if isinstance(opponent, Truck):
                        distance, smash = opponent.special_move()
                        if smash:
                            opponent_lane = vehicles.index(opponent)
                            for i in range(opponent.get_position(), min(opponent.get_position() + distance, TRACK_LENGTH)):
                                track[opponent_lane][i] = '-'
                    else:
                        distance = opponent.special_move()
                elif random.random() < 0.7:  # 70% chance of fast move
                    distance = opponent.fast()
                else:
                    distance = opponent.slow()

                opponent_lane = vehicles.index(opponent)
                if track[opponent_lane][min(opponent.get_position() + distance, TRACK_LENGTH - 1)] == '0' and not isinstance(opponent, Truck):
                    opponent._position -= distance // 2

    winner = max(vehicles, key=lambda v: v.get_position())
    print(f"\nThe winner is {winner._name}!")

main()
