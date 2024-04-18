import sys
import numpy as np
from Encryption import Encryption  # Assuming Encryption is a base class in another module

class HillCipher(Encryption):
    key_string = "FAIL"  # Initial key string

    def __init__(self, key_matrix, key_string,
                 modValue=26, 
                 removeSpace=True,          # Option to remove spaces
                 encryptSpace=False,        # Option to encrypt spaces
                 encryptSymbol=True,        # Option to encrypt symbols
                 upperCaseAll=True,         # Option to convert all to uppercase
                 ) -> None:
        # Initialize with parameters and call to parent class constructor
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, self.key_string, key_matrix)
        self.mod = modValue
        self.key_matrix = self.construct_key_matrix()  # Construct the key matrix
        self.name = "Hill Cipher"  # Name of the cipher method

    def construct_key_matrix(self):
        # Converts the key string into numerical values and reshapes it into a matrix
        key_values = [ord(char) - ord('A') for char in self.key_string]
        key_matrix = np.array(key_values).reshape(2, 2)
        # Check if the matrix is invertible under mod
        if np.linalg.det(key_matrix) % self.mod == 0:
            raise ValueError("Key matrix must be invertible under modulo")
        return key_matrix

    def encrypt(self, plainText):
        # Prepares text for encryption by converting to uppercase and removing non-alpha characters
        plain_text = ''.join([char.upper() for char in plainText if char.isalpha()])
        # Ensures text length is even for matrix operations
        if len(plain_text) % 2 != 0:
            plain_text += 'X'  # Append 'X' if text length is odd

        encryptedText = ""
        # Encrypts text by pairs of characters
        for i in range(0, len(plain_text), 2):
            pair = [ord(char) - ord('A') for char in plain_text[i:i+2]]
            result = np.dot(self.key_matrix, pair) % self.mod
            encryptedText += ''.join(chr(int(r) + ord('A')) for r in result)

        return encryptedText

    def decrypt(self, cipherText):
        decryptedText = ""
        # Calculate the inverse of the key matrix for decryption
        inverse_key = np.linalg.inv(self.key_matrix)
        det = int(round(np.linalg.det(self.key_matrix)))  # Calculate the determinant
        det_inv = pow(det, -1, self.mod)  # Find modular inverse of the determinant
        inverse_key = (inverse_key * det_inv) % self.mod  # Adjust inverse key using the mod

        # Decrypts text in pairs
        for i in range(0, len(cipherText), 2):
            pair = [ord(char) - ord('A') for char in cipherText[i:i+2]]
            result = np.dot(inverse_key, pair) % self.mod
            decryptedText += ''.join(chr(int(r) + ord('A')) for r in result)

        return decryptedText

def main():
    key_string = "ABCD"
    key_matrix = [[6, 25], [1, 3]]  # Example of an invertible matrix under modulo
    cipher = HillCipher(key_matrix, key_string)

    plaintext = "get_state"
    print("Original Plaintext:", plaintext)
    encrypted_text = cipher.encrypt(plaintext)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
    
