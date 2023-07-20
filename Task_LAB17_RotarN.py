dic_hydrogen = dict(name='Hydrogen', symbol='H', number=1)


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

    # def __str__(self):
    #     print(self.name, self.symbol, self.number)


hydrogen1 = Element('hydrogen', 'H', 1)
hydrogen1.dump()

hydrogen2 = Element('hydrogen', 'H', 1)
hydrogen2.__str__()