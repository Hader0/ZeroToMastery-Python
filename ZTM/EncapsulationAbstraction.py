class MyselfAndI:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def announce(self):
        print(f'My name is {self.name} and I am {self.age} years old!')


myself = MyselfAndI('Hayden', 20)

myself.announce()