from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def main():
    # Create instances of each vehicle type
    car = Car("Speed Demon", "C", 10, 30)
    motorcycle = Motorcycle("Road Rocket", "M", 15, 35)
    truck = Truck("Heavy Hauler", "T", 5, 25)

    print("Testing Car:")
    print(f"Initial nitro: {car.get_nitro()}")
    for _ in range(4):
        car.move()
    
    print("\nTesting Motorcycle:")
    print(f"Initial lean angle: {motorcycle.get_lean_angle()}")
    motorcycle.lean(30)
    print(f"New lean angle: {motorcycle.get_lean_angle()}")
    motorcycle.move()
    
    print("\nTesting Truck:")
    print(f"Initial cargo: {truck.get_cargo()}")
    truck.load_cargo(20)
    print(f"Cargo after loading: {truck.get_cargo()}")
    truck.move()
    truck.unload_cargo(10)
    print(f"Cargo after unloading: {truck.get_cargo()}")
    truck.move()

if __name__ == "__main__":
    main()
