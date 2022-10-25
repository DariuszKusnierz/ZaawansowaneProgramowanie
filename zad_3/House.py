from Property import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot
        pass

    def __str__(self) -> str:
        return f'Dom o powierzchni {self.area}, z liczbą pokoi: {self.rooms}, kosztuje {self.price}. Znajduje się on pod adresem {self.address}, a cała działka ma powierzchnię {self.plot}m^2.'
