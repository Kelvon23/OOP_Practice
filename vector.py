#Understand Requirments:
"""
Create a Vector class and the instances should have 3 attributes x,y,z w no defaults 

It wants me to create a text represention of my instance in way it that helps user reconstruct
the isinstance


Magnitute - I think from my understanding it want me to be calcualte the magnitue of this problem
through use of only 1 mehtod ?


We need to allow users a way to add vectors together 


We need to allow users a way to do scalar multiiplication operation in a way that order of operands 
dont matter

All comparison operations should be supported between 2 instnace of Vector


vector should be hashable 


boolean logic for vectors should be false only for when magnitude is Zero

we want to be able to allow vector have subscript feature in which it allows them to Index and 
return the value in that postion


"""
from functools import total_ordering
from math import sqrt 

@total_ordering
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return Vector(new_x,new_y,new_z)

    def __mul__(self, other):
        new_x = self.x * other
        new_y = self.y * other
        new_z = self.z * other

        return Vector (new_x,new_y,new_z)

    def __abs__(self):

        magnitude = sqrt(self.x**2 + self.y ** 2 + self.z ** 2)

        return magnitude

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)
        

    def __getitem__(self, key):
        key = key.lower()

        if key == "x":
            return self.x
        elif key == "y":
            return self.y
        elif key == "z":
            return self.z
        else:
            raise KeyError(key)

    def __hash__(self):
        return hash(abs(self))
    def __repr__(self):
        return F"Vector({self.x},{self.y},{self.z})"

    def __bool__(self):
        return abs(self)!=0
    
