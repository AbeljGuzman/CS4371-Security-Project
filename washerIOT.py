from IOTdevice import IOTDevice
from data.config import *

# Washer IOT device simulator
class Washer(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        self._state = "off"
        self._mode = "normal"
        self._temperature = "cold"
        self._running = "stopped"
    
    # sets the state of the washer
    # set_state;on or set_state;off
    def set_state(self, state):
        if state in ["on", "off"]:
            self._state = state
            return "200"  # Success code
        else:
            raise Exception("invalid message", state)

    # sets the mode of the washer (washer must be on to set mode)
    # set_mode;<normal, delicate, heavy, quick>
    def set_mode(self, mode):
        if self._state == "off":
            raise Exception("off")
        if mode in ["normal", "delicate", "heavy", "quick"]:
            self._mode = mode
            return "200"  # Success code
        else:
            raise Exception("invalid message", mode)
    
    # sets the temperature of the washer (washer must be on to set temperature)
    # set_temperature;<cold, warm, hot>
    def set_temperature(self, temperature):
        if self._state == "off":
            raise Exception("off")
        if self.is_valid_temperature(temperature):
            self._temperature = temperature
            return "200"  # Success code
        else:
            raise Exception("invalid temperature", temperature)

    # starts the washer (washer must be on to start)
    # start_wash
    def start_wash(self):
        if self._state == "off":
            raise Exception("off")
        if self._running == "stopped":
            self._running = "running"
            return "200"  # Success code
        else:
            raise Exception("Washer already running")

    # stops the washer (washer must be on to stop)
    # stop_wash
    def stop_wash(self):
        if self._state == "off":
            raise Exception("off")
        if self._running == "running":
            self._running = "stopped"
            return "200"  # Success code
        else:
            raise Exception("Washer already stopped")
    
    # returns the state of the washer
    def get_state(self):
        return self._state

    # returns the mode of the washer
    def get_mode(self):
        if self._state == "off":
            raise Exception("off")
        return self._mode
    
    # returns the temperature of the washer
    def get_temperature(self):
        if self._state == "off":
            raise Exception("off")
        return self._temperature

    # returns whether the washer is running
    def is_running(self):
        if self._state == "off":
            raise Exception("off")
        return self._running
    
    # checks if the temperature is valid
    def is_valid_temperature(self, temperature):
        # Define valid temperature settings
        valid_temperatures = ["cold", "warm", "hot"]
        return temperature in valid_temperatures
    
    # maps commands to their respective functions
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
    washer = Washer("7") # initialize washer IOT device
    washer.setEncryption(KEY, upperCaseAll=False, removeSpace=False) # set encryption
    
    print("Setting up a new Smart Washer..")
    input_ip = WASHER_IP # ensure IP is configured in config
    input_port = WASHER_PORT # ensure port is configured in config

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
