import sys

import numpy as np

from Encryption import Encryption


class HillCipher(Encryption):
    key_string = "FAIL"

    def __init__(self, key_matrix, key_string,
                 modValue = 26, 
                 removeSpace=True,          # Remove space
                 encryptSpace=False,         # Encrypt Space
                 encryptSymbol=True,        # Encypt Symbol
                 upperCaseAll=True,        # Uppercase ALL
                 ) -> None:
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, self.key_string, key_matrix)
       # self.key_string = key_string
        self.mod = modValue
        self.key_matrix = self.construct_key_matrix()
        self.name = "Hill Cipher"

    def construct_key_matrix(self):
        key_values = [ord(char) - ord('A') for char in self.key_string]
        key_matrix = np.array(key_values).reshape(2, 2)
        if np.linalg.det(key_matrix) % self.mod == 0:
            raise ValueError("Key matrix must be invertible under modulo")
        return key_matrix



    def encrypt(self, plainText):
        # Process text
        plain_text = ''.join([char.upper() for char in plainText if char.isalpha()])
        if len(plain_text) % 2 != 0:
            plain_text += 'X'  # Append 'X' to ensure even length for pairs

        encryptedText = ""
        for i in range(0, len(plain_text), 2):
            pair = [ord(char) - ord('A') for char in plain_text[i:i+2]]
            result = np.dot(self.key_matrix, pair) % self.mod
            encryptedText += ''.join(chr(int(r) + ord('A')) for r in result)

        return encryptedText

    def decrypt(self, cipherText):
        decryptedText = ""
        inverse_key = np.linalg.inv(self.key_matrix)  # Calculate inverse
        det = int(round(np.linalg.det(self.key_matrix)))  # Determinant
        det_inv = pow(det, -1, self.mod)  # Modular inverse of the determinant

        inverse_key = (inverse_key * det_inv) % self.mod  # Adjusted inverse key

        for i in range(0, len(cipherText), 2):
            pair = [ord(char) - ord('A') for char in cipherText[i:i+2]]
            result = np.dot(inverse_key, pair) % self.mod
            decryptedText += ''.join(chr(int(r) + ord('A')) for r in result)

        return decryptedText

def main():
    key_string = "ABCD"
    key_matrix = [[6, 25], [1, 3]]  # Ensure this matrix is invertible under modValue
    cipher = HillCipher(key_matrix, key_string)

    plaintext = "get_state"
    print("Original Plaintext:", plaintext)
    encrypted_text = cipher.encrypt(plaintext)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
    