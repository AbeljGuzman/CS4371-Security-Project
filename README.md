# Security-Project-Group-3



## Members:
# Danny Pham
# Abel Guzman
# Dylan Eiseman
# Justin Balarbar
# Blake Woods

*Instructions to run*
Dependency:
python3, numpy, pillow
Setup the config file:
Navigate to `./data/config.py`
Change all the IPs to your IP address
EX:
```
HUB_IP = “197.154.207.225”

SPEAKER_IP = “197.154.207.225”
SMARTLIGHT_IP = “197.154.207.225”
SMARTCAR_IP = “197.154.207.225”
WASHER_IP = “197.154.207.225”
		```
Leave the device ports as they are
Execute Hub: `python hubUI.py`
A GUI will pop up in another window
Execute Speaker:
Open up a new terminal and execute `python speakerIOT.py`
Execute SmartCar:
Open up a new terminal and execute `python SmartCarIOT.py`
Execute SmartLight:
Open up a new terminal and execute `python smartLightIOT.py`
Execute Washer:
Open up a new terminal and execute `python washerIOT.py`
Register Devices in Hub:
Go back to Hub
Enter the ID (arbitrary), IP (your IP), and port for all 4 IOT devices.


	
EX:
		```
		Device ID: Washer
		Device IP: “197.154.207.225”
		Device Port: 8086
		```
Note that the IP and Port must match the values in `./data/config.py`
Click on [Add Device]
The new device will show up at the bottom of the Hub
Send a Command:
Click on [Send Message]. A new window will pop up
Enter the ID and Message
		```
		Device ID: my_speaker
		Message: get_status
		```
Click on [Send] and observe the returned response in the Hub GUI
Available commands are listed below for each device:
Speaker:
get_state
set_state;on/off (state must be “on” to set the device status & volume)


get_status
set_status;connected/not connected


get_volume
set_volume;(0-10)
	      - 	SmartCar:
		      -	get_state
		      -	set_state;on/off (state can either be on or off to set the cars status & speed)

		      -	get_status
		      -	set_status;determines whether the car is locked or unlocked

		      -	get_speed
		      -	set_speed;(0-200) must be inputted as values of 25
      - 	SmartLight:
		       -	get_state
		      -	set_state;on/off(state must be “on” to set the device brightness & color)

		      -	get_brightness
		      -	set_brightness; must range from 0 - 100

		      -	get_color
		      -	set_color; base color is “white” but can be changed
      - 	Washer:
		       -	get_state
		      -	set_state;on/off(state must be “on” to set the device mode & temperature)

		      -	get_mode
		      -	set_mode;<delicate,heavy,quick>

		      -	get_temperature
		      -	set_temperature;<cold, warm, hot>


		      -	start_wash
		      -	stop_wash
	 

Multi-Device Testing:
Follow the steps above for each other Devices
Use a new computer instead of a new terminal window for each IOT Device
Remember to set the IP addresses

Simulated Attack:
Open up `WireShark` and set the filter to `udp.port == 8080`, where `8080` is the Hub’s port number is set in `config.py`
Note the message is encrypted at the bottom right
*Functionalities*
	HUB: IoT Communication 
The Hub and IoT devices can communicate bi-directionally over a local network using UDP/TCP.
	User:
The user is able to operate the IoT devices using the Hub.
	Attacker:
The attacker is able to use WireShark to sniff and inspect the packets being sent.
	Encryption/Decryption:
All communication between the Hub and IoT devices are encrypted and decrypted upon sending and receiving.
We have implemented the Substitution Cipher and are working on adding the Hill Cipher as well.
	Authentication:
Devices must be registered by the user through the Hub (Through GUI).
*Files we created for the project*
	SmartCarIOT.py:
Simulates a Smart Car IoT device.
	SmartLightIOT.py:
Simulates a Smart Light IoT device.
	SpeakerIOT.py:
Simulates a Speaker IoT device.
	WasherIOT.py:
Simulates a Washer IoT device.
	Substitution.py:
Provides Substitution Cipher for each device.
	Hill.py:
Provides Hill Cipher for each device. (NOT FULLY WORKING)

Hill Cipher:
     -	Development for the project initially started with Hill cipher, but we were unable to get it fully working, so we opted for the monoalphabetic substitution cipher. Our Hill cipher was moved to the Hill branch in the GitHub repo to be run separately. 
     -	The Hill cipher works well with letters but struggles with spaces, semicolons, and underscores because it can't turn these symbols into numbers as it does with letters. This makes it less useful when these symbols are important. We tried to fix it by increasing the range of the mod value and creating a custom alphabet, but this led to many errors, so we couldn't do this. We also tried making the matrix a 3x3 and 4x4, but it still wouldn't encrypt the message in WireShark.


References
	Celik, Z. B., Babun, L., Sikder, A. K., Aksu, H., Tan, G., McDaniel, P., & Uluagac, A. S. (2018). Sensitive Information Tracking in Commodity IoT. Retrieved from https://arxiv.org/pdf/1802.08307v1.pdf

	Celik, Z. B., Babun, L., Sikder, A. K., Aksu, H., Tan, G., McDaniel, P., & Uluagac, A. S. (2018). Sensitive Information Tracking in Commodity IoT. In Proceedings of the USENIX Security Symposium. Baltimore, MD. Retrieved from https://github.com/IoTBench/

	Hoover, B., Hsu, J., Pradhan, M., Valdez, A., & Vu, V. (2023). Smart-Home [Software]. Bitbucket. Retrieved from https://bitbucket.org/cs4371compsecurity/smart-home/src/master/
