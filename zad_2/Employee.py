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
