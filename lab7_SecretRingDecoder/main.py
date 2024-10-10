import check_input
import caesar
import cipher

""" Secret Decoder Ring

Written by: Sena Matsuzoe, Rianne Papa
Date: 10/09/2024

The program allows the user to encrypt or decrypt messages using different types of encryption methods. Encrypted messages
will read from the console then written to file called 'message.txt' , and decrypted messages will be read from said file then
display to console.

This program supports two encryption methods: Atbash and Caesar cipher.

"""

def main():
    """
    1. Displays main menu
    2. Select 1 or 2 for encrypt or decrypt respectively
    3. Writes encrypted string to 'message.txt' or reads decrypted string from 'message.txt'
    """
    print("Secret Decoder Ring:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = check_input.get_int_range("Choose an option: ", 1, 2)

    if choice == 1:
        message = input("Enter message: ")
        print("Choose encryption type:")
        print("1. Atbash")
        print("2. Caesar")

        cipher_choice = check_input.get_int_range("Choose an option: ", 1, 2)

        if cipher_choice == 1:
            selected_cipher = cipher.Cipher()
        else:
            shift = check_input.get_int_range("Enter shift value (0-25): ", 0, 25)
            selected_cipher = caesar.Caesar(shift)

        encrypted_message = selected_cipher.encrypt_message(message)

        with open("message.txt", "w") as file:
            file.write(encrypted_message)
        print("Encrypted message saved to 'message.txt'.")

    elif choice == 2:
        print("Choose decryption type:")
        print("1. Atbash")
        print("2. Caesar")

        cipher_choice = check_input.get_int_range("Choose an option: ", 1, 2)

        if cipher_choice == 1:
            selected_cipher = cipher.Cipher()
        else:
            shift = check_input.get_int_range("Enter shift value (0-25): ", 0, 25)
            selected_cipher = caesar.Caesar(shift)

        with open("message.txt", "r") as file:
            encrypted_message = file.read()

        decrypted_message = selected_cipher.decrypt_message(encrypted_message)
        print(f"Decrypted message: {decrypted_message}")

main()
