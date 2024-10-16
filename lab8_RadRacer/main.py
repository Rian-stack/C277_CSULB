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
    
    c = car.Car("Lightning Car", "C", 6, 8)
    m = motorcycle.Motorcycle("Swift Bike", "M", 6, 8)
    t = truck.Truck("Behemoth Truck", "T", 4, 8)
    vehicles = [c, m, t]

    for i, vehicle in enumerate(vehicles, 1):
        print(f"{i}. {vehicle.description()}")

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)

    player = vehicles[choice - 1]
    player._initial = 'P'

    track = create_track()

    while all(v.get_position() < TRACK_LENGTH for v in vehicles):
        print("\n" + "\n".join(str(v) for v in vehicles))
        display_track(track, vehicles)

        # Player's turn
        action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        player_lane = vehicles.index(player)
        next_obstacle = next((i for i in range(player.get_position() + 1, TRACK_LENGTH) if track[player_lane][i] == '0'), TRACK_LENGTH)
        distance_to_obstacle = next_obstacle - player.get_position()

        if action == 1:
            result = player.fast(distance_to_obstacle)
        elif action == 2:
            result = player.slow(distance_to_obstacle)
        else:
            distance = player.special_move()
            if isinstance(player, truck.Truck):
                for i in range(player.get_position(), min(player.get_position() + distance, TRACK_LENGTH)):
                    track[player_lane][i] = '-'
            result = f"({player._name}) uses special move and travels {distance} units!"

        print(result)

        # AI turns
        for opponent in vehicles:
            if opponent != player:
                opponent_lane = vehicles.index(opponent)
                next_obstacle = next((i for i in range(opponent.get_position() + 1, TRACK_LENGTH) if track[opponent_lane][i] == '0'), TRACK_LENGTH)
                distance_to_obstacle = next_obstacle - opponent.get_position()

                if random.random() < 0.2:  # 20% chance of special move
                    distance = opponent.special_move()
                    if isinstance(opponent, truck.Truck):
                        for i in range(opponent.get_position(), min(opponent.get_position() + distance, TRACK_LENGTH)):
                            track[opponent_lane][i] = '-'
                elif random.random() < 0.7:  # 70% chance of fast move
                    opponent.fast(distance_to_obstacle)
                else:
                    opponent.slow(distance_to_obstacle)

    winner = max(vehicles, key=lambda v: v.get_position())
    print(f"\nThe winner is {winner._name}!")

if __name__ == "__main__":
    main()
