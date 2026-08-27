import random 


class Student:
    educational_platform = "udemy"
    def __init__(self,name,age=20):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [
            "Hi, I'm ",
            "Hey there, my name is ",
            "Hi. Oh, my name is "
                        ]

        print(f"{random.choice(greetings)} {self.name}") 









def main():

    students = ["John","Bruce","Peter"]

    for student in students:
        Student(student).greet()

    



if __name__ == "__main__":
    main()