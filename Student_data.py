
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a student")