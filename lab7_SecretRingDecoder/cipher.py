class Cipher:
    '''
    The superclass representing a ciper. Used for encryption and decryption of messages.
    This is an implementation of an Atbash cipher which changes the corresponding letter
    to a reversed alphabet. 
    
    e.g.
    A -> Z, B -> Y etc.
    
    Attributes:
        alphabet (list): A list of uppercase letters A-Z used for substitution-based ciphers.
    '''

    def __init__(self):
        """
        Initializes the Cipher object with an alphabet attribute consisting of uppercase letters A-Z.
        """
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def encrypt_message(self, message):
        """
        Encrypts the provided message by converting it to uppercase and encrypting each letter.
        Non-alphabetic characters are left unchanged.
        
        Args:
            message (str): The message to be encrypted.
        
        Returns:
            str: The encrypted message.
        """
        encrypted_message = ""
        message = message.upper()  # Convert the message to uppercase
        
        for char in message:
            if char in self.alphabet:
                encrypted_message += self._encrypt_letter(char)  # Encrypt letter
            else:
                encrypted_message += char  # Leave non-letters unchanged
        return encrypted_message

    def decrypt_message(self, message):
        """
        Decrypts the provided message by converting it to uppercase and decrypting each letter.
        Non-alphabetic characters are left unchanged.
        
        Args:
            message (str): The message to be decrypted.
        
        Returns:
            str: The decrypted message.
        """
        decrypted_message = ""
        message = message.upper()  # Convert the message to uppercase
        
        for char in message:
            if char in self.alphabet:
                decrypted_message += self._decrypt_letter(char)  # Decrypt letter
            else:
                decrypted_message += char  # Leave non-letters unchanged
        
        return decrypted_message

    def _encrypt_letter(self, letter):
        """
        Encrypts a single letter by looking up its position in the alphabet and reversing it.
        
        Args:
            letter (str): The letter to be encrypted.

        Returns:
            str: The encrypted letter.
        """
        pos = self.alphabet.index(letter)
        return self.alphabet[25 - pos]

    def _decrypt_letter(self, letter):
        """
        Decrypts a single letter by reversing its position in the alphabet, based on the encryption rules.
        
        Args:
            letter (str): The letter to be decrypted.

        Returns:
            str: The decrypted letter.
        """
        pos = self.alphabet.index(letter)
        return self.alphabet[25 - pos]
