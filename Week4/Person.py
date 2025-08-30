
class Person:
    

    def __init__(self, name, address, age, id,grade):
    
        self.__name = name
        self.__address = address
        self.__age = age
        self.__id = id
        self.__grade = grade

    # --- Getters ---
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__id
    
    
    def get_grade(self):
        return self.__grade
    
    # --- Setters ---
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        if age > 0: 
            self.__age = age
        else:
            print("Invalid age! Age must be positive.")

    def set_id(self, id):
        self.__id = id

    def set_grade(self, grade):
        self.__grade = grade

   
    def show_details(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")
        print(f"ID: {self.__id}")
       


