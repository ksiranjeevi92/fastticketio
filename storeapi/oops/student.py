class Student:
    def __init__(self, new_name: str, new_grades: list[int]):
        self.name = new_name
        self.grades = new_grades

    def averge(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("One Student Name", [45, 89, 70, 45])


print(student_one.__class__)
