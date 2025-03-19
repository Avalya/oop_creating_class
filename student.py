class Student:
    def __init__(self, name=None, student_id=None, major=None, gpa=None):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def display_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")
        print("-" * 20)

    def is_honor_student(self):
        if self.gpa is not None and self.gpa >= 3.5:
            return True
        else:
            return False

if __name__ == "__main__":
    students = []
    n = int(input("Enter the number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i + 1}:")
        name = input("Name: ")
        student_id = input("Student ID: ")
        major = input("Major: ")
        gpa = float(input("GPA: "))

        student = Student(name, student_id, major, gpa)
        students.append(student)

    print("\nStudent Details:")
    for student in students:
        student.display_info()
        if student.is_honor_student():
            print(f"{student.name} is an honor student.")
        else:
            print(f"{student.name} is not an honor student.")
            