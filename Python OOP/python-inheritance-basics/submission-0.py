class SmartDevice:
    def __init__(self, name: str):
        self.name = name

class SmartLight(SmartDevice):
    def turn_on(self) -> None: 
        print("Smart Light is turned on")
    def turn_off(self) -> None: 
        print("Smart Light is turned off")
# TODO: Implement the SmartLight class


# Don't change the code below
device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()
