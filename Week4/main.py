from Student import Student
from Person import Person

def main():
    student1 = Student("Oshadee", "Auckland", 28, "CT15008","B")
    parent = Person("John", "Christchurch", 35, "CT15034","C")

    print("=== Student Details ===")
    student1.show_student_details()

    print("\n=== Parent Details ===")
    parent.show_details()

    print("\nUpdating student's address and age...")
    student1.set_address("Wellington")
    student1.set_age(29)
    student1.set_grade("A+")

    print("\n=== Updated Student Details ===")
    student1.show_student_details()


if __name__ == "__main__":
    main()

