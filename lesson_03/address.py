class Address:
    def __init__(self, ind, city, street, house, apart):
        self.ind = ind
        self.city = city
        self.street = street
        self.house = house
        self.apart = apart

    def __str__(self):
        return f"{self.ind}, {self.city}, {self.street}, {self.house} - {self.apart}"
