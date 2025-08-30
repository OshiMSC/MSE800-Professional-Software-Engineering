from Student import Student
from Person import Person

def main():
    student1 = Student("Oshadee", 28,"Auckland","CT15008")
    parent = Person("john",35,"Chrischurch","CT15034")
    print("Student")
    student1.show_Student_details()
    parent.show_details()

if __name__ == "__main__":
    main()
