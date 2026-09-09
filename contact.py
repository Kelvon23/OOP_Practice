# #Undrstand:

# #What are the requirements ? 

# It wants me to create a class that has instance attributes that make up a contact like first,last name, phone number, email, display_mode

# Users Should be able to only use first and last name to create the instance 

# The rules of equality between objects are:

#     phone or email are specificed and the same 

#     first and last name are the same

# A method for instance representation that will display info of the instance depending on the what mode is the display_mode is on:

#     mask = showing obfuscated instance first and last name 
#     unmasked = showing the attributes of the instance in full 

# Unmasked by using format 


# str method should output first letter of last and first NameError



Planning - 

eq:

First need to know if user provided phone or email to then check for equality 

while name and last name are always given so i don't need a check 





class Contact:

    def __init__(self,First_Name,Last_Name,Phone_Number = None ,Email = None ,Display_Mode = "masked"):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Display_Mode = Display_Mode

    def __eq__(self, other):
        if self.Phone_Number is not None and other.Phone_Number is not None:
            return self.Phone_Number == other.Phone_Number
        elif self.Email is not None and other.Email is not None:
            return self.Email == other.Email
        else:
            return self.First_Name == other.First_Name and self.Last_Name == other.Last_Name



        
        
        



