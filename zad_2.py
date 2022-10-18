from dbm.ndbm import library


class Libraby:
    def __init__(self,city,street,zip_code,open_hours,phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        pass

    def __str__(self) -> str:
        return f'Biblioteka w mieście {self.city} ulica {self.street} kod pocztowy {self.zip_code}, otwarta w godzinach {self.open_hours}, tel: {self.phone}.'
        pass

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        pass

    def __str__(self) -> str:
        return f'Pracownik: {self.first_name} {self.last_name}, zatrudniony {self.hire_date}, a urodzony {self.birth_date}, mieszka w mieście {self.city} ulica {self.street} kod pocztowy {self.zip_code}, tel: {self.phone}.'
        pass

class Book:
    def __init__(self,library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        pass

    def __str__(self) -> str:
        return f'Książka z {self.library} została wydana {self.publication_date}, przez {self.author_name} {self.author_surname} i posiada {self.number_of_pages} stron.'
        pass

class Order:
    def __init__(self, employee, student, books, order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        pass

    def __str__(self) -> str:
        return f'Zamówienie realizowane przez {self.employee} dla studenta {self.student} obejmuje następujące książki: {self.books}. Data zamówienia: {self.order_date}.'
        pass

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

library_1 = Libraby("Katowice","Kościuszki 12", "11-111", "12-18", 123345567)
library_2 = Libraby("Gliwice","Sienkiewicza 5", "12-121", "10-17", 923345561)

book_1 = Book(library_1, "05.10.2011", "Tadeusz", "Nowak", 115)
book_2 = Book(library_2, "08.01.1994", "Ewa", "Krawczyk", 86)
book_3 = Book(library_1, "24.06.2021", "Teresa", "Mróz", 93)
book_4 = Book(library_1, "11.04.2008", "Edward", "Mocny", 215)
book_5 = Book(library_2, "13.11.2003", "Mateusz", "Wąs", 75)

employee_1 = Employee("Mariusz", "Kowalski", "15.03.2018", "24.12.1999", "Katowice","Kościuszki 14", "11-111", 332345567)
employee_2 = Employee("Ewa", "Wolna", "21.08.2021", "01.05.1987", "Gliwice","Sienkiewicza 18", "12-121", 392349567)
employee_3 = Employee("Arkadiusz", "Lipski", "09.05.2020", "21.09.2001", "Katowice","Warszawska 3", "11-131", 632346567)

student_1 = Student("Marek", [40,11])