from database import create_student_table,create_course_table,create_departments_table,create_lectures_table,create_subjects_table
from students import add_user, view_users, search_user, delete_user
from courses import add_course,view_course,search_course,delete_course
from lectures import add_lectures,view_lectures,search_lectures,delete_lectures
from subjects import add_subjects,view_subjects,search_subjects,delete_subjects
from departments import add_departments,view_departments,search_departments,delete_departments
def menu():
    print("\n==== Wellcome TO Yoobee College Main System ====")
    print("1. Manage Students Details")
    print("2. Manage Lecturer Details")
    print("3. Manage Course Details")
    print("4. View Subjects You needs to learn")
    print("5. Get to know about departments")
    print("6. Exit")

def main():
    create_student_table()
    create_lectures_table()
    create_course_table()
    create_departments_table()
    create_subjects_table()


    
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            print("\n==== Wellcome TO Students Module ====")
            print("1. View Students Details")
            print("2. Register New Student")
            print("3. Search students by name")
            print("4. Delete Student by student id")
            print("5. Main Menu")

            subChoice = input("Select an option (1-5): ")
            if subChoice == '1':
                students = view_users()
                for student in students:
                    print(student)

            elif subChoice == '2':
                StudentName = input("Enter Student's Name:").strip()
                student_email = input("Enter Student'Email:").strip()
                phone = input("Enter Student's contact number:").strip()
                address = input("Enter Student's Address:").strip()
                department_ID = input("Enter Student's Department Details:").strip()
                course_ID = input("Enter Student's Course Details:").strip()
                add_user(StudentName,student_email,phone,address,department_ID,course_ID)

            elif subChoice == '3':
                Stu_name = input("Enter name to search: ")
                students = search_user(Stu_name)
                for student in students:
                    print(student)
            elif subChoice == '4':
                stu_id = int(input("Enter student ID to delete: "))
                delete_user( stu_id)
            elif choice == '5':
                print("Good Bye..")
            else :
                menu()
        elif choice == '2':
            print("\n==== Wellcome TO Lecrturer's Module ====")
            print("1. View Lecturer Details")
            print("2. Register New Lecturer")
            print("3. Search Lecturer by name")
            print("4. Delete Lecturer by Id")
            print("5.Exit")
            subChoice = input("Select an option (1-5): ")
            if subChoice == '1':
                lecturers = view_lectures()
                for lec in lecturers:
                    print(lec)

            elif subChoice == '2':  
                lecturer_Name = input("Enter Lecturer Name:").strip()
                lecturer_Email = input("Enter Lecturer Email:").strip()
                department_ID = input("Enter Department Id:").strip()
                course_ID = input("Enter Course Id:").strip()
                add_lectures(lecturer_Name,lecturer_Email,department_ID,course_ID)
            elif subChoice == '3':
                lecturerName= input("Enter name to search: ")
                lecturers = search_lectures(lecturerName)
                for lec in lecturers:
                    print(lec)
            elif subChoice == '4':
                lecturer_Id = int(input("Enter lecturer ID to delete: "))
                delete_lectures( lecturer_Id)
            elif choice == '5':
                print("Goodbye!")
            break
        elif choice == '3':
            print("\n==== Wellcome TO Course Module ====")
            print("1. View Course Details")
            print("2. Register New Course")
            print("3. Search Course  by name")
            print("4. Delete Course by Id")
            print("5.Exit")
            subChoice = input("Select an option (1-5): ")
            if subChoice == '1':
                courses = view_course()
                for course in courses:
                    print(course)

            elif subChoice == '2':  
                course_Name = input("Enter Course Name:").strip()
                duration = input("Enter Lecturer Email:").strip()
                department_ID = input("Enter Department Id:").strip()
                add_course(course_Name,duration,department_ID)
            elif subChoice == '3':
                course_Name= input("Enter name to search: ")
                courses = search_course(course_Name)
                for course in courses:
                    print(course)
            elif subChoice == '4':
                course_Id = int(input("Enter Course ID to delete: "))
                delete_course( course_Id)
            elif choice == '5':
                print("Goodbye!")
            break

    #SUBJECTS
        elif choice == "4":
            print("\n==== Wellcome TO Subject Module ====")
            print("1. View Subject Details")
            print("2. Register New Subject")
            print("3. Search Subject by name")
            print("4. Delete Subject by Id")
            print("5.Exit")
            subChoice = input("Select an option (1-5): ")
            if subChoice == '1':
                subjects = view_subjects()
                for sub in subjects:
                    print(sub)

            elif subChoice == '2':  
                subject_Name = input("Enter Subject Name:").strip()
                course_ID = input("Enter Course Id:").strip()
                add_subjects(subject_Name,course_ID)
            elif subChoice == '3':
                subject_Name= input("Enter name to search: ")
                subjects = search_subjects(subject_Name)
                for sub in subjects:
                    print(sub)
            elif subChoice == '4':
                subject_ID= int(input("Enter Subject ID to delete: "))
                delete_subjects( subject_ID)
            elif choice == '5':
                print("Goodbye!")
            break

      #DEPARTMENTS  
        elif choice == "5":
            print("\n==== Wellcome TO Department Module ====")
            print("1. View Department Details")
            print("2. Register New Department")
            print("3. Search Department by name")
            print("4. Delete Department by Id")
            print("5.Exit")
            subChoice = input("Select an option (1-5): ")
            if subChoice == '1':
                departments = view_departments()
                for dept in departments:
                    print(dept)

            elif subChoice == '2':  
                department_Name = input("Enter Department Name:").strip()
                add_departments(department_Name)
            elif subChoice == '3':
                department_Name= input("Enter name to search: ")
                departments = search_departments(department_Name)
                for dept in departments:
                    print(dept)
            elif subChoice == '4':
                department_ID= int(input("Enter Department ID to delete: "))
                delete_subjects(department_ID)
            elif choice == '5':
                print("Goodbye!")
            break
        elif choice == "6":
            print("End of the process")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
