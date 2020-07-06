# Polymorphism - You can change the outcome of the method in child class

from Student_data import Student


class Devops(Student):
    def __init__(self, first_name, last_name, stream): # This adds an attribute "stream" to the devops sub class.
        self.first_name = first_name
        self.last_name = last_name
        self.stream = stream

    def roll_call(self):
        print(f"I am a {self.stream} Student")
        # This is the same method as the parent class, however it has slightly changed functionality


# Code demo
person_one = Student("Daniel", "Teegan")
person_two = Devops("Daniel", "Teegan", "Devops")

person_one.roll_call() # Here we are calling the same class but they have 2 differant outcomes.
person_two.roll_call()

