class Encryption:
    upperCaseAll = None
    removeSpace = None
    encryptSpace = None
    encryptSymbol = None
    reverseText = None
    key = None
    key_matrix = None
    name = "Main"
    alphabet = None
    
    def __init__(self, key, key_matrix,removeSpace=True, encryptSpace=False, encryptSymbol=False, upperCaseAll=True, reverseText=False) -> None:
        self.removeSpace = removeSpace
        self.encryptSpace = encryptSpace
        self.encryptSymbol = encryptSymbol
        self.upperCaseAll = upperCaseAll
        self.reverseText = reverseText
        self.key = "FAIL"
        self.key_matrix = key
        self.alphabet = self.defineAlphabet()
        
    def defineAlphabet(self):
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ:_"
    
    def describe(self):
        return {
            "name" : self.name 
        }
        
    def getSettings(self):
        return {
            "Space Removed" : self.removeSpace,
            "Space Encrypt" : self.encryptSpace,
            "Symbol Encrypt" : self.encryptSymbol
        }
    
    
    def applySettings(self, plainText):
        # Remove spaces if required
        if self.removeSpace:
            plainText = plainText.replace(" ", "")
        
        # Convert text to uppercase if required
        if self.upperCaseAll:
            plainText = plainText.upper()
        
        # Reverse the text if required
        if getattr(self, 'reverseText', False):  # Ensure reverseText attribute exists
            plainText = plainText[::-1]

        # Calculate non-alphabetic character indices
        non_alpha_indices = [i for i, char in enumerate(plainText) if not char.isalpha()]

        return plainText, non_alpha_indices
            
    def encrypt(self, plainText):
        pass

    def decrypt(self, cipherText):
        pass
    
    def deleteSpace(self, plainText):
        return plainText.replace(" ", "")
    
    def convertToUppercase(self, plainText):
        return plainText.upper()
    
    def reverseString(self, text):
        return ''.join(reversed(text))


