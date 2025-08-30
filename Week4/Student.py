from Person import Person

class Student(Person):

    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age, student_id)  # ✅ Pass student_id as id
        self.student_id = student_id

    def show_Student_details(self):
        print("Greetings and Felicitations from Mastero " + self.name)
        print("Student ID:", self.student_id)
        print("Address:", self.address)
        print("Age:", self.age)


class Juniors(Person):
    def __init__(self, name, address, age, temporary_id):
        super().__init__(name, address, age, temporary_id)  # ✅ Pass temporary_id as id
        self.temporary_id = temporary_id

    def show_junior_details(self):
        super().show_details()  # ✅ Correct method name
        print("Temporary Id:", self.temporary_id)
