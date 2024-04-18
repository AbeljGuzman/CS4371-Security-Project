from IOTdevice import IOTDevice
from data.config import *

class SpeakerIOT(IOTDevice):
    state = None
    status = None
    volume = None
    
    def __init__(self, id):
        super().__init__(id)
        self.state = "off"
        self.status = "Not Connected"
        self.volume = 0
        
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        if state == "on" or state == "off":
            self.state = state
            return "200"
        else:
            raise Exception("Invalid State: ", state)
    
    def get_status(self):
        return self.status
    
    def set_status(self, state):
        if self.state == "off":
            raise Exception("Device is off")
        if state == "Connected" or state == "Not Connected":
            self.status = state
            return "200"
        else:
            raise Exception("Invalid Status: ", state)
    
    def get_volume(self):
        return str(self.volume)
    
    def set_volume(self, volume):
        if self.state == "off":
            raise Exception("Device is off")
        volumeLvl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if volume in volumeLvl:
            self.volume = int(volume)
            return "200"
        else:
            raise Exception("Invalid Volume choice: ", volume)
        
    def process_command(self, command, message=None):
        mapper = {
            'get_state': self.get_state,
            'set_state': self.set_state,
            'get_stat{s': self.get_status,
            'get_status': self.get_status,
            'set_status': self.set_status,
            'get_volume': self.get_volume,
            'set_volume': self.set_volume
        }
           
        return mapper[command](message) if message else mapper[command]()
        
    
    
if __name__ == "__main__":
    speaker = SpeakerIOT("1010")
    speaker.setEncryption(KEY, upperCaseAll=False, removeSpace=False)

    print("Setting up a new Smart Speaker..")
    input_ip = SPEAKER_IP
    input_port = SPEAKER_PORT
    speaker.init_sockets(input_ip, input_port)
    
    print("Receiving......")
    response = speaker.receive()
    command, message = speaker.parse_command(response) 
    print("Command: ", command)
    print("Message: ", message)
    
    while command != "exit": 
        output = speaker.process_command(command, message)  

        print("Response sent to HUB")        
        speaker.send(output, (HUB_IP, HUB_PORT))
        print("Receiving......")
        response = speaker.receive()
        command, message = speaker.parse_command(response)
        
    print("Goodbye")