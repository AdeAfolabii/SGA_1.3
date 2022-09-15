# create a car
class Car:
    def __init__(self, type, model, colour, seats, transmission):
        self.type = type
        self.model = model
        self.colour = colour
        self.seat = seats
        self.transmission = transmission

    def car_type (self):
        return self.type

    def car_model (self):
        return self.model

    def car_colour (self):
        return self.colour

    def car_seat (self):
        return self.seat

    def car_transmission (self):
        return self.transmission

a = Car("minivan", "corsa", "blue", 6 , "manual")
b = Car("convertible", "audi r8", "red", 2, "automatics")

print(a.car_type()), print(b.car_type())
print(a.model), print(b.model)
print(a.colour), print(b.colour)
print(a.seat), print(b.seat)
print(a.transmission), print(b.transmission)