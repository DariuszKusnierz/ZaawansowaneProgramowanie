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

    def __str__(self) -> str:
        return f'{self.name} z ocenami: {self.marks}'
        pass
