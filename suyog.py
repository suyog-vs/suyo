traffic_light = "Green"


speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)

class Car(Vehicle):
    def _init_(self, make):
        self.make = make

    def start_engine(self):
        message = "Car engine started."
        print(message)

class Bike(Vehicle):
    def _init_(self, bike_type):
        self.type = bike_type

    def start_engine(self):
        message = "Bike engine started."
        print(message)


print("Global Variable: traffic_light =", traffic_light)
print("Module Variable: speed_limit =", speed_limit)

car = Car("Toyota")
bike = Bike("Mountain")

print("Object Variable: Car make =", car.make)
print("Object Variable: Bike type =", bike.type)

car.start_engine()
bike.start_engine()