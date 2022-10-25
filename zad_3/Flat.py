from Property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor
        pass

    def __str__(self) -> str:
        return f'Mieszkanie o powierzchni {self.area}, z liczbą pokoi: {self.rooms}, kosztuje {self.price}. Znajduje się ono pod adresem {self.address}, na {self.floor} piętrze.'
