class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        pass

    def __str__(self) -> str:
        return f'Książka z {self.library} została wydana {self.publication_date}, przez {self.author_name} {self.author_surname} i posiada {self.number_of_pages} stron.'
        pass
