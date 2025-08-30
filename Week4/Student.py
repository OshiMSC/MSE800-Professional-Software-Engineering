from Person import Person

class Student(Person):


    def __init__(self, name, address, age, student_id,grade):
        super().__init__(name, address, age, student_id,grade) 
        self.__student_id = student_id
        self.__grade = grade

    # Getter and Setter for student_id
    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id
        self.set_id(student_id) 

    def show_student_details(self):
        print("Greetings and Felicitations from Mastero", self.get_name())
        print("Student ID:", self.__student_id)
        print("Address:", self.get_address())
        print("Age:", self.get_age())
        print("Grade:", self.get_grade())


    def get_grade(self):
        return self.__grade

    def updated_info(self,grade):
        self.__grade = grade
        self.set_grade(grade)


class Juniors(Person):
  

    def __init__(self, name, address, age, temporary_id,grade):
        super().__init__(name, address, age, temporary_id,grade)
        self.__temporary_id = temporary_id

    def get_temporary_id(self):
        return self.__temporary_id
    
    def get_grade(self):
        return self.__grade

    def set_temporary_id(self, temp_id):
        self.__temporary_id = temp_id
        self.set_id(temp_id) 

    def set_grade(self, grade):
        self.__grade = grade
        self.set_grade(grade) 

    def show_junior_details(self):
        super().show_details()
        print("Temporary ID:", self.__temporary_id)
        print("Grade:", self.__grade)
