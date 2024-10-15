from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
import check_input

def main():
    # Create instances of each vehicle type
    car = Car("Speed Demon", "C", 10, 30)
    motorcycle = Motorcycle("Road Rocket", "M", 15, 35)
    truck = Truck("Heavy Hauler", "T", 5, 25)

    print("Testing Car:")
    print(f"Initial nitro: {car.get_nitro()}")
    moves = check_input.get_positive_int("Enter number of moves for the car: ")
    for _ in range(moves):
        car.move()
    
    print("\nTesting Motorcycle:")
    print(f"Initial lean angle: {motorcycle.get_lean_angle()}")
    lean_angle = check_input.get_int_range("Enter lean angle (-45 to 45 degrees): ", -45, 45)
    motorcycle.lean(lean_angle)
    print(f"New lean angle: {motorcycle.get_lean_angle()}")
    motorcycle.move()
    
    print("\nTesting Truck:")
    print(f"Initial cargo: {truck.get_cargo()}")
    cargo_load = check_input.get_positive_int("Enter amount of cargo to load: ")
    truck.load_cargo(cargo_load)
    print(f"Cargo after loading: {truck.get_cargo()}")
    truck.move()
    cargo_unload = check_input.get_positive_int("Enter amount of cargo to unload: ")
    truck.unload_cargo(cargo_unload)
    print(f"Cargo after unloading: {truck.get_cargo()}")
    truck.move()

if __name__ == "__main__":
    main()
