class Garage:
    def __init__(self) -> None:
        self.cars = []

    def __getitem__(self, index):
        return self.cars[index]

    def __len__(self):
        return len(self.cars)

    def __repr__(self):
        return f"Garage is {self.cars}"

    def __str__(self):
        return f"Garge len is {len(self)}"


ford = Garage()

ford.cars.append("Fiesta")
ford.cars.append("Traveller")


print(ford)
