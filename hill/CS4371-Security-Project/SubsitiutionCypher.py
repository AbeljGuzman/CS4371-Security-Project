import random
from Encryption import Encryption

class SubstitutionCipher(Encryption):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key = self.generate_substitution_key()

    def generate_substitution_key(self):
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        shuffled_letters = random.sample(letters, len(letters))
        return dict(zip(letters, shuffled_letters))

    def encrypt(self, plain_text):
        plain_text, _ = self.applySettings(plain_text)
        encrypted_text = ''
        for char in plain_text:
            if char in self.key:
                encrypted_text += self.key[char]
            else:
                encrypted_text += char  # Non-alphabetic characters are not changed
        return encrypted_text

    def decrypt(self, cipher_text):
        reversed_key = {v: k for k, v in self.key.items()}
        decrypted_text = ''
        for char in cipher_text:
            if char in reversed_key:
                decrypted_text += reversed_key[char]
            else:
                decrypted_text += char  # Non-alphabetic characters are not changed
        return decrypted_text
