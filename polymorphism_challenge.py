
''' Activity 2: Polymorphism Challenge! 🎭
   
Create a program that includes animals or vehicles with the same action (like move()). 
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).'''

# Base class for vehicles
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on water.")

# Create objects of each vehicle
vehicle1 = Car()
vehicle2 = Plane()
vehicle3 = Boat()

# Demonstrating polymorphism - calling the same method on different objects
vehicle1.move()  # Car
vehicle2.move()  # Plane
vehicle3.move()  # Boat