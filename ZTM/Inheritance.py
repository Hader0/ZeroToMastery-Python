class User():
    email = 'hey@gmail.com'
    def signIn(self):
        print("Logged in")

# Subclasses of Class User
class Wizard(User): # By passing the parent class, we're able to use the children functions
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def powerAttack(self):
        print(f'"Boom" occured from {self.name}\'s {self.power}')

class Archer(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        

    def powerAttack(self):
        print(f'"WHAM" occured from {self.name}\'s {self.power}')

wizard1 = Wizard('Greg', 'Lightning')
archer1 = Archer('Alice', 'Telekinesis')

wizard1.powerAttack()

archer1.powerAttack()