class Student:
    def __init__(self, first_name):
        self.first_name = first_name


    #define getter method
    @property
    def get_name(self):
        return self.first_name

student = Student("Monica")
print(student.first_name)
print(student.get_name)