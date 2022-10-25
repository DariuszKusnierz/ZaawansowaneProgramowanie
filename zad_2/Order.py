class Order:
    def __init__(self, employee, student, books, order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        pass

    def __str__(self) -> str:
        return f'Zamówienie realizowane przez {self.employee} dla studenta {self.student} obejmuje następujące książki: {self.books} Data zamówienia: {self.order_date}.'
        pass
