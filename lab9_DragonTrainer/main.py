import random
import entity
import check_input
from dragon import Dragon
from hero import Hero

def main():
    dragon = Dragon("Gronkle", 100, 3)
    hero = Hero("Astrid", 50)

    while dragon.is_alive() and hero.is_alive():
        print(f"\n{dragon}")
        print(f"{hero}\n")

        attack_choice = check_input.get_int_range("Choose your attack (1 for basic, 2 for special): ", 1, 2)
        if attack_choice == 1:
            print(hero.basic_attack(dragon))
        elif attack_choice == 2:
            print(hero.special_attack(dragon))

        if dragon.is_alive() and dragon._special_attacks > 0:
            print(dragon.basic_attack(hero))
            dragon.decrement_special_attacks()

        if not dragon.is_alive():
            print(f"\n{hero.get_name()} has defeated {dragon.get_name()}!")
        elif not hero.is_alive():
            print(f"\n{dragon.get_name()} has defeated {hero.get_name()}!")

if __name__ == "__main__":
    main()