# Assignment 1 
class FlightComputer: 
    def __init__( self, sensor, power, function):
        self.sensor = sensor
        self.power = power
        self.function = function

    def state(self):
        print("This " + self.sensor + " is working")

    def battery(self):
        print("Its " + self.power + " !")

class AdvancedFlightComputer(FlightComputer):
    def __init__(self, sensor, power, function):
        super().__init__(sensor, power, function)

        
class MilitaryFlightComputer(AdvancedFlightComputer):
    def __init__(self, sensor, power, function):
        super().__init__(sensor, power, function)
    def power_status(self):
        if self.power == "On":
            return "hoorah!"
        else:
            return "power off"

fc_1 = AdvancedFlightComputer("MPU", "Off", "Orientation")
fc_2 = MilitaryFlightComputer("GPS", "On", "Location")
print(fc_2.power_status())
fc_1.state()

fc_2.battery()

print(fc_2.power)
print(fc_1.function)

# Assignment 2

class Cat():
    def sound(self):
        print("This is a cats sound")

class Lion(Cat):
    def sound(self):
        print("A lion roars!")

class Kitty(Cat):
    def sound(self):
        print("A kitty meows!")

cats = [Lion(), Kitty()]
for c in cats:
    c.sound()
