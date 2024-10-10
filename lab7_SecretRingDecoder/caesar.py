import cipher

class Caesar(cipher.Cipher):
    """
    A subclass of the Cipher class that represents a Caesar cipher, which shifts letters by a given value.

    e.g.
    If shift = 3 
    ABCDEF -> DEFGHI

    Attributes:
        alphabet (list): Inherited from Cipher, a list of uppercase letters A-Z.
        shift (int): The shift value used for encrypting and decrypting letters.
    """
    def __init__(self, shift):
        """
        Initializes the Caesar cipher with a specified shift value.

        Args:
            shift (int): The number of positions each letter in the alphabet is shifted.
        
        Raises:
            ValueError: If the shift value is not an integer.
        """
        super().__init__()
        self.shift = shift

    def _encrypt_letter(self, letter):
        """
        Encrypts a single letter by applying the Caesar shift.

        Args:
            letter (str): The letter to be encrypted.

        Returns:
            str: The encrypted letter.
        """
        pos = self.alphabet.index(letter)
        shifted_pos = (pos + self.shift) % 26
        return self.alphabet[shifted_pos]

    def _decrypt_letter(self, letter):
        """
        Decrypts a single letter by reversing the Caesar shift.

        Args:
            letter (str): The letter to be decrypted.

        Returns:
            str: The decrypted letter.
        """
        pos = self.alphabet.index(letter)
        shifted_pos = (pos - self.shift) % 26
        return self.alphabet[shifted_pos]
