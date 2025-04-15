''' Assignment 1: Design Your Own Class! 🏗️

Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

    '''


# Base class
class EmergencyCall:
    def __init__(self, caller_name, location):       # Initialize attributes
        self.caller_name = caller_name               # Name of the caller
        self.location = location                     # Location of the emergency

    def respond(self):                               # Respond method to be overridden
        print(f"📞 Emergency call from {self.caller_name} at {self.location}. Sending help!")    

class PoliceEmergency(EmergencyCall):                # Inherits from EmergencyCall
    def respond(self):                               # Override the respond method
        print(f"🚓 Police dispatched to {self.location}. Caller: {self.caller_name}")

class FireEmergency(EmergencyCall):
    def respond(self):
        print(f"🔥 Firefighters sent to {self.location} immediately! Caller: {self.caller_name}")

class MedicalEmergency(EmergencyCall):
    def respond(self):
        print(f"🚑 Ambulance is on the way to {self.location} for {self.caller_name}")

# Create objects
call1 = PoliceEmergency("Lebo", "Johannesburg")
call2 = FireEmergency("Thandi", "Durban")
call3 = MedicalEmergency("Sipho", "Cape Town")

for call in [call1, call2, call3]:
    call.respond()

