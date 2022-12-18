# print(len("Hello"))
# print(len([10,20,30]))

# def add(x,y,z = 0):
#     return x+y+z


# print(add(3,4))
# print(add(3,4,5))

# class car:
#     pass
# car11=car


class Vehicle:
    def __init__(self, name, milage):
        self.name = name
        self.milage = milage
        
class bus(Vehicle):
        pass

obj = bus("ABC",10)
print(obj.milage, obj.name)