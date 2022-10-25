from Libraby import Libraby
from Book import Book
from Employee import Employee
from Student import Student
from Order import Order


library_1 = Libraby("Katowice", "Kościuszki 12", "11-111", "12-18", 123345567)
library_2 = Libraby("Gliwice", "Sienkiewicza 5", "12-121", "10-17", 923345561)

book_1 = Book(library_1, "05.10.2011", "Tadeusz", "Nowak", 115)
book_2 = Book(library_2, "08.01.1994", "Ewa", "Krawczyk", 86)
book_3 = Book(library_1, "24.06.2021", "Teresa", "Mróz", 93)
book_4 = Book(library_1, "11.04.2008", "Edward", "Mocny", 215)
book_5 = Book(library_2, "13.11.2003", "Mateusz", "Wąs", 75)

employee_1 = Employee("Mariusz", "Kowalski", "15.03.2018", "24.12.1999", "Katowice", "Kościuszki 14", "11-111", 332345567)
employee_2 = Employee("Ewa", "Wolna", "21.08.2021", "01.05.1987", "Gliwice", "Sienkiewicza 18", "12-121", 392349567)
employee_3 = Employee("Arkadiusz", "Lipski", "09.05.2020", "21.09.2001", "Katowice", "Warszawska 3", "11-131", 632346567)

student_1 = Student("Marek", [40, 11])
student_2 = Student("Ania", [19, 70, 50])
student_3 = Student("Kasia", [11, 9, 81])

order_1 = Order(employee_1, student_1, book_1, "21.09.2022")
order_2 = Order(employee_2, student_2, book_2, "11.05.2022")

print(order_1)
print(order_2)
