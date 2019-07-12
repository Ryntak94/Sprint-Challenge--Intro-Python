# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass

    #this is the base class to FlightVehicle and GroundVehicle

class FlightVehicle(Vehicle):
    pass
    #this is the base class for Starship and Airplane
    #the base class for this class is Vehicle

class Starship(FlightVehicle):
    pass
    #the base class for this class is FlightVehicle

class Airplane(FlightVehicle):
    pass
    #the base class for this class is FlightVehicle

class GroundVehicle(Vehicle):
    pass
    #the base class for this class is Vehicle
    #this is the base class for Car and Motorcycle

class Motorcycle(GroundVehicle):
    pass
    #the base class for this class is GroundVehicle

class Car(GroundVehicle):
    pass
    #the base class for this class is GroundVehicle
