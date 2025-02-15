class Student:

    def __init__(self):
        self.first_name = "Patryk"
        self.last_name = "Ziajka"
        self.age = 54

def run_example():
    student = Student()


    student.first_name = "Andrzej"
    student.last_name = "Nowak"
    student.age = 30
    print(student.first_name)
    print(student.last_name)
    print(student.age)

if __name__ == '__main__':
    run_example()