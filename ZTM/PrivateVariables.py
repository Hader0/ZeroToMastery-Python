class MyselfAndI:
    def __init__(self, name, age, lastName):
        self.name = name
        self.age = age
        self._lastName = lastName # It's agreed upon in the python community to 
                                   # not change the variables starting with an underscore

    def announce(self):
        print(f'My name is {self.name} and I am {self.age} years old!')


myself = MyselfAndI('Hayden', 20)

myself.announce()