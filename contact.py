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



# Planning - 

# Control Flow Pattern:

#  when there are multiple independent ways to succeed, don’t return failure 
# until you’ve exhausted all the possible ways to succeed

# eq:

# Control Flow: Failed Inequality Rule doesn't mean the objects aren't equal to each 
# other. It just means the particular rule didn't prove that their equal, so keep checking.
# Only once we reach to last rule of equality we can accept w.e output is 






class Contact:

    def __init__(self,First_Name,Last_Name,Phone_Number = None ,Email = None ,Display_Mode = "masked"):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Display_Mode = Display_Mode

    def __eq__(self, other):
        #refactor this shii later 
        if ( 
            self.Phone_Number is not None 
            and other.Phone_Number is not None 
            and self.Phone_Number == other.Phone_Number):
            return True
        elif (
            self.Email is not None 
            and other.Email is not None 
            and self.Email == other.Email) :
            return True
        else:
            return self.First_Name == other.First_Name and self.Last_Name == other.Last_Name


    def __str__(self):
        return f"{self.Last_Name[0]}{self.First_Name[0]}"

    def __repr__(self):
        pass

    



        
        
        



