
class Person:
    """Represents a general person with basic details."""
    
    def __init__(self,name,address,age,id):
        self.name = name
        self.age = age
        self.id = id
        self.address= address
        
    def show_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Age:", self.age)
        print("ID:", self.id)

