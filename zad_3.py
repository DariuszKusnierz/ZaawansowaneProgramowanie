class Property:
    def __init__(self, area, rooms, price, address) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        pass


class House(Property):
    def __init__(self, area, rooms, price, address, plot) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot
        pass

    def __str__(self) -> str:
        return f'Dom o powierzchni {self.area}, z liczbą pokoi: {self.rooms}, kosztuje {self.price}. Znajduje się on pod adresem {self.address}, a cała działka ma powierzchnię {self.plot}m^2.'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor
        pass

    def __str__(self) -> str:
        return f'Mieszkanie o powierzchni {self.area}, z liczbą pokoi: {self.rooms}, kosztuje {self.price}. Znajduje się ono pod adresem {self.address}, na {self.floor} piętrze.'


house = House("80m^2", 5, "12500000zł", "Tczew ul. Parkowa 15", 125)
flat = Flat("25m^2", 5, "1500000zł", "Tczew ul. Parkowa 8", 2)

print(house)
print(flat)
