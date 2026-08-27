#Understand 
#Input - a string that should have format of YYYY-MM-DD
#Constraints - assume user born 12:00 am and td would be 12:00 am 
#Edge Cases - empty, what if a str appears in one of them, uncessary symbols,
#Output - print out of a string in english of number of minutes the user been alive as of today. 
#Planning
#Low Level - I will create 3 functions that will do seperate jobs. The first function will be used to validate the dob user input and return an object with correct format or else return an exit message. The second function will
# do the calculation and convert the days into minutes and return total minutes. Last function will transforn the total mintues into english words and format in away that doesn't have any 'and' in there. 
# 
#High Level - For function 1 I will be validating the input from the user. I intend to use regex to enforce the formating that the questions ask YYYY-MM-DD. If regex comes back and fails then we should go straight to exit.sys call. From there
# I will use the extracted pieces and transform them into int so it can work for when we start to create the time object. I will use a try and except for when we start to do the creation of object as it raises a value Error if the date
# doesn't make logically sense. And of course if it failed it will exit. Overall the idea is validate the format first through the use of regex and then have the object validate the date and at the end if all works then we will create the object.
# Moving on for Function 2 we will be now focus on caculating the DOB with td curr day. My function will recieve an arugemnt from function 1 with the new date object and inside the function we will create a new object that will represent
# curr date. Then from there we will try to do an operator overload in which the moduel already does for us and do the math curr - dob. Lastly we will do conversion from days to actual minutes (fomural Days*24*60) and 
# return that final answer. 
#
#Implemenation -

from datetime import date
import inflect
import sys
import re


def main():
    user_input=input("YYYY-MM-DD: ")
    time_object=create_time_object(user_input)
    mins=caculate_mins(time_object)
    print_final_result(mins)

def create_time_object(DOB):
    pattern = r"^(?P<Year>\d\d\d\d)-(?P<Month>\d\d)-(?P<Day>\d\d)$"
    match = re.search(pattern,DOB)

    if match:
        Year=int(match.group('Year'))
        Month= int(match.group('Month'))
        Day = int(match.group('Day'))
    else:
        sys.exit("Invalid Date")

    try:
        user_dob = date(Year,Month,Day)
        curr_date = date.today()
        if user_dob > curr_date:
            sys.exit("Invalid Date")
        return user_dob

    except ValueError:
        sys.exit("Invalid Date")

    

        

def caculate_mins(user_dob):
    curr_date= date.today()

    difference_object =  curr_date - user_dob
    days = difference_object.days

    conversion_days_to_mins = days * 24 * 60

    return conversion_days_to_mins


def print_final_result(mins):
    p = inflect.engine()
    formated_mins = p.number_to_words(mins, andword="")
    print(f"{formated_mins} minutes")




...


if __name__ == "__main__":
    main()