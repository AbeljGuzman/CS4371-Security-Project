from IOTdevice import IOTDevice
from data.config import *

class SmartLight(IOTDevice):
    def __init__(self, id):
        super().__init__(id)
        self._state = "off"  
        self._brightness = 0  
        self._color = "white"

    def set_state(self, state):
        if state in ["on", "off"]:
            self._state = state
            return "200"  # success code
        else:
            raise Exception("invalid message", state)

    def set_brightness(self, brightness):
        print(f"Received brightness input: {brightness} of type {type(brightness)}")  # Debug: Check the input type and value
        
        if self._state == "off":
            raise Exception("Device is off")

        try:
            brightness = int(brightness)
        except ValueError:
            raise Exception("Invalid message", brightness)

        if 0 <= brightness <= 100:
            self._brightness = brightness
            return "200"
        else:
            raise Exception("Invalid message", brightness)
        
    def set_color(self, color):
        if self._state == "off": 
            raise Exception("off")
        self._color = color
        return "200"  # success code

    def get_state(self):
        return self._state

    def get_brightness(self):
        if self._state == "off": 
            raise Exception("off")
        return str(self._brightness)

    def get_color(self):
        if self._state == "off": 
            raise Exception("off")
        return self._color

    def process_command(self, command, message=None):
        try:
            mapper = {
                'set_state': self.set_state,
                'set_brightness': self.set_brightness,
                'set_color': self.set_color,
                'get_state': self.get_state,
                'get_brightness': self.get_brightness,
                'get_color': self.get_color,
            }
            return mapper[command](message) if message else mapper[command]()

        except Exception as e:
            exception = e.args[0]
            if exception == "off":
                return "ERROR: device currently off"
            elif exception == "invalid message":
                return f"ERROR: '{e.args[1]}' message not valid"
            else:
                return f"ERROR: {e}"

def main():
    light = SmartLight("2")  
    light.setEncryption(KEY, upperCaseAll=False, removeSpace=False)

    print("Setting up a new Smart Light..")
    input_ip = SMARTLIGHT_IP  # Ensure you have this configured in your config file
    input_port = SMARTLIGHT_PORT  # Ensure this is also configured

    light.init_sockets(input_ip, input_port)

    print("Receiving command from Hub")

    # Receive, parse, and process command from Hub
    command = light.receive()
    while command != "exit":
        command, message = light.parse_command(command)
        output = light.process_command(command, message)

        print("Sending output to Hub")

        # Send returned output to Hub
        light.send(output, (HUB_IP, HUB_PORT))

        print("Receiving command from Hub")

        command = light.receive()

if __name__ == '__main__':
    main()