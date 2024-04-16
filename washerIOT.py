from IOTdevice import IOTDevice
from data.config import *

class Washer(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        self._state = "off"
        self._mode = "normal"
        self._temperature = "cold"
        self._running = "stopped"
    
    def set_state(self, state):
        if state in ["on", "off"]:
            self._state = state
            return "200"  # Success code
        else:
            raise Exception("invalid message", state)

    def set_mode(self, mode):
        if self._state == "off":
            raise Exception("off")
        if mode in ["normal", "delicate", "heavy", "quick"]:
            self._mode = mode
            return "200"  # Success code
        else:
            raise Exception("invalid message", mode)
    
    def set_temperature(self, temperature):
        if self._state == "off":
            raise Exception("off")
        if self.is_valid_temperature(temperature):
            self._temperature = temperature
            return "200"  # Success code
        else:
            raise Exception("invalid temperature", temperature)

    def start_wash(self):
        if self._state == "off":
            raise Exception("off")
        if self._running == "stopped":
            self._running = "running"
            return "200"  # Success code

    def stop_wash(self):
        if self._state == "off":
            raise Exception("off")
        if self._running == "running":
            self._running = "stopped"
            return "200"  # Success code
        
    def get_state(self):
        return self._state

    def get_mode(self):
        if self._state == "off":
            raise Exception("off")
        return self._mode
    
    def get_temperature(self):
        if self._state == "off":
            raise Exception("off")
        return self._temperature

    def is_running(self):
        if self._state == "off":
            raise Exception("off")
        return self._running
    
    def is_valid_temperature(self, temperature):
        # Define valid temperature settings
        valid_temperatures = ["cold", "warm", "hot"]
        return temperature in valid_temperatures
    

    def process_command(self, command, message=None):
        try:
            mapper = {
                'set_state': self.set_state,
                'set_mode': self.set_mode,
                'set_temperature': self.set_temperature,
                'start_wash': self.start_wash,
                'stop_wash': self.stop_wash,
                'get_state': self.get_state,
                'get_mode': self.get_mode,
                'get_temperature': self.get_temperature,
                'is_running': self.is_running,
            }
            return mapper[command](message) if message else mapper[command]()
        except Exception as e:
            exception = e.args[0]
            if exception == "off":
                return "ERROR: device currently off"
            elif exception == "invalid message":
                return f"ERROR: '{e.args[1]}' message not valid"
            else:
                return f"ERROR: {e} command not defined"

def main():
    washer = Washer(4)
    washer.setEncryption(KEY, upperCaseAll=False, removeSpace=False)
    
    print("Setting up a new Smart Washer..")
    input_ip = WASHER_IP
    input_port = WASHER_PORT

    washer.init_sockets(input_ip, input_port)

    print("Receiving command from Hub")
    command = washer.receive()
    while command != "exit":
        command, message = washer.parse_command(command)    
        output = washer.process_command(command, message)
        
        print("Sending output to Hub")
        washer.send(output, (HUB_IP, HUB_PORT))
        
        print("Receiving command from Hub")
        command = washer.receive()

if __name__ == '__main__': 
    main()