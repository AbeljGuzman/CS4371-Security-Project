import random
from Encryption import Encryption

# Substitution Cipher class
class SubstitutionCipher(Encryption):

    def __init__(self,
                 removeSpace=False,
                 encryptSpace=True,
                 encryptSymbol=True,
                 upperCaseAll=False,
                 reverseText=False) -> None:
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, reverseText)
        self.name = "Substitution Cipher"
        self.substitution_dict = {
            'a': 'q',
            'b': 'w',
            'c': 'e',
            'd': 'r',
            'e': 't',
            'f': 'y',
            'g': 'u',
            'h': 'z',
            'i': 'o',
            'j': 'p',
            'k': 'a',
            'l': 's',
            'm': 'd',
            'n': 'f',
            'o': 'g',
            'p': 'h',
            'q': 'j',
            'r': 'k',
            's': 'l',
            't': 'i',
            'u': 'x',
            'v': 'c',
            'w': 'v',
            'x': 'b',
            'y': 'n',
            'z': 'm'
        }

    # encrypts the plain text using the substitution cipher
    def encrypt(self, plainText):
        plain = plainText
        encryptedMessage = ""
        for letter in plain.lower():
            if letter in self.substitution_dict:
                encryptedMessage += self.substitution_dict[letter]
            else:
                encryptedMessage += letter
        
        return encryptedMessage
    
    # decrypts the cipher text using the substitution cipher
    def decrypt(self, cipherText):
        cipher = cipherText

        decryptedMessage = ""
        for char in cipher:
            if char in self.substitution_dict.values():
                for key, value in self.substitution_dict.items():
                    if value == char:
                        decryptedMessage += key
            else:
                decryptedMessage += char

        return decryptedMessage
