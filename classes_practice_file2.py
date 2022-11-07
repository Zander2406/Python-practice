STUDENT_LIST = []

class Student:
    def __init__(self, name=None, roll_no=None, marks1=None, marks2=None):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, name, roll_no, marks1, marks2):
        student = Student(name, roll_no, marks1, marks2)
        STUDENT_LIST.append(student)

    def display(self, student):
        print(f"Name: {student.name}\nRoll No: {student.roll_no}\nMarks1: {student.marks1}\nMarks2: {student.marks2}")




if __name__ == "__main__":
    StudentX = Student()
    StudentX.accept("Ankit", 26, 80, 88)
    StudentX.accept("Swarnava", 56, 88, 89)
    StudentX.display(STUDENT_LIST[0])



