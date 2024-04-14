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
        plain_text = self.applySettings(plainText)
        #plain_text = ''.join(plain_text) 
        
        if len(plain_text) % 2 != 0:
            plain_text += 'Z'
            
        encryptedText = ""

        for i in range(0, len(plain_text), 2):
            pair = [ord(char) - ord('A') for char in plain_text[i:i+2]]
            result = np.dot(self.key_matrix, pair) % self.mod
            encryptedText += ''.join([chr(result[j] + ord('A')) for j in range(2)])
        
        
        '''
        #msgMatrix = [[ord(char) - 65] for char in plain_text]
        msgMatrix = [[ord(char)-65]for string in plain_text for char in string]
        keyMatrix = [[ord(char) - 65 for char in self.key[:2]], [ord(char) - 65 for char in self.key[2:4]]]

    
        for i in range(0,len(msgMatrix),2):
            resultMatrix = [[0],[0]]
        for j in range(2):
            for k in range(1):
                for l in range(2):
                    resultMatrix[j][k] += keyMatrix[j][l] * msgMatrix[l + i][k]
        for j in range(2):
            resultMatrix[j][0] %= self.mod

        for j in range(2):
            encryptedText += chr(resultMatrix[j][0] + 65)
    '''
        return encryptedText
    
    def decrypt(self, cipherText):
        decryptedText = ""

        inverse_key = np.linalg.inv(self.key_matrix)
        inverse_key = np.round(inverse_key *np.linalg.det(self.key_matrix) * np.linalg.det(inverse_key) ** -1).astype(int) % self.mod

        for i in range(0, len(cipherText), 2):
            pair = [ord(char) - ord('A') for char in cipherText[i:i+2]]
            result = np.dot(inverse_key, pair) % self.mod
            decryptedText += ''.join([chr(result[j] + ord('A')) for j in range(2)])

        return decryptedText

    

    