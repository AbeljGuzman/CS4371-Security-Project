from Hill import HillCipher


class Communicator:
    key = None
    id = None
    ip = None
    port = None
    commSocket = None
    cipher = None
    enableEncryption = False
    buf = 512
    

    def __init__(self, id, key):
        self.key = "FAIL"
        self.id = id
        self.enableEncryption = False
    
    def encrypt(self, message):
        if self.enableEncryption: 
            encrypted_message = self.cipher.encrypt(message)
            return encrypted_message
        else:
            return message
    
    def decrypt(self, encrypted_message):
        if self.enableEncryption:
            decrypted_message = self.cipher.decrypt(encrypted_message)
            return decrypted_message
        else:
            return encrypted_message
    
    

    def send(self, message, recipient):
        pass


    def receive(self):
        return


    def process_command():
        return

    # setters
    def setIP(self, ipaddr):
        self.ip = ipaddr

    def setPort(self, portNumber):
        self.port = portNumber

    def setSocket(self, socket):
        self.commSocket = socket
    '''    
    def setEncryption(
        self,
        key_string,
        removeSpace=True,          # Remove space
        encryptSpace=False,         # Encrypt Space
        encryptSymbol=False,        # Encypt Symbol
        upperCaseAll=True,        # Uppercase ALL
        reverseText = False    # Reverse Plain text
    ):
        self.enableEncryption = True
        self.cipher = HillCipher(key_string)
        self.cipher.removeSpace = removeSpace
        self.cipher.encryptSpace = encryptSpace
        self.cipher.upperCaseAll = upperCaseAll
        self.cipher.reverseText = reverseText
        self.cipher.encryptSymbol = encryptSymbol
    '''
    def setEncryption(self, key,key_matrix, **kwargs):
        self.enableEncryption = True
        self.cipher = HillCipher(key_string=self.key,key_matrix = self.key,**kwargs)

    def compress_img(self, img_data):
        return img_data
    
    def decompress_img(self, compress_data):
        return compress_data
