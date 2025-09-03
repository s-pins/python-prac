class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return "A vehicle can move"
    
class Car(Vehicle):
    def move(self):
        return f"Driving a {self.brand} car."
    
class Motorcycle(Vehicle):
    def move(self):
        return f"Riding a {self.brand} motorcycle."

car = Car("Ferrari")
moto = Motorcycle("Kawasaki")
print(car.move())
print(moto.move())