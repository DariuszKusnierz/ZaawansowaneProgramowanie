class Libraby:
    def __init__(self, city, street, zip_code, open_hours, phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        pass

    def __str__(self) -> str:
        return f'Biblioteka w mieście {self.city} ulica {self.street} kod pocztowy {self.zip_code}, otwarta w godzinach {self.open_hours}, tel: {self.phone}.'
        pass
