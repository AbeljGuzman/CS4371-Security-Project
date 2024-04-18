from data.config import *
from IOTdevice import IOTDevice

class SmartCar(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        # Initialize any specific attributes for a smart car
        self.state = "off"
        self.status = "locked"
        self.speed = "0"
        
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        if state in ["on", "off"]:
            self.state = state
            return "200"
        else:
            raise Exception("Invalid State: ", state)
        
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        if status in ["locked", "unlocked"]:
            self.status = status
            return "200"
        else:
            raise Exception("Invalid Status: ", status)
        
    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        if self.state == "off":
            raise ValueError("Car is off")
        mph = ['0', '25', '50', '75', '100', '125', '150', '175', '200']
        if speed in mph:
            self.speed = int(speed)
            return "200"
        else:
            raise ValueError("Invalid Speed: ", speed)
        
    def process_command(self, command, message=None):
        mapper = {
            'get_state': self.get_state,
            'set_state': self.set_state,
            'get_status': self.get_status,
            'set_status': self.set_status,
            'get_speed': self.get_speed,
            'set_speed': self.set_speed
        }
        
        return mapper[command](message) if message else mapper[command]()
    
if __name__ == "__main__":
    smartcar = SmartCar("1212")
    smartcar.setEncryption(KEY, upperCaseAll = False, removeSpace = False)
    
    print("Warming up the Smart Car..")
    input_ip = SMARTCAR_IP
    input_port = SMARTCAR_PORT
    
    smartcar.init_sockets(input_ip,input_port)
    
    print("Receiving......")
    response = smartcar.receive()
    command, message = smartcar.parse_command(response) 
    print("Command: ", command)
    print("Message: ", message)
    
    while command != "exit": 
        output = smartcar.process_command(command, message)  

        print("Response sent to HUB")        
        smartcar.send(output, (HUB_IP, HUB_PORT))
        print("Receiving......")
        response = smartcar.receive()
        command, message = smartcar.parse_command(response)
        
    print("Goodbye")