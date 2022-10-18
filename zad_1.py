class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        pass

    def is_passed(self) -> bool:
        mean = 0
        for mark in self.marks:
            mean += mark
        mean /= len(self.marks)
        return mean > 50

student2 = Student("Ania", [60,70,50])
print(student2.is_passed())

student1 = Student("Marek", [10,15,30])
print(student1.is_passed())
