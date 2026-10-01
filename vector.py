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






class Vector:
    def __init__(x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __getitem__(self, key):
        pass

    def __repr__(self):
        pass

    def __bool__(self):
        pass
