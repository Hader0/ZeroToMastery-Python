class User():
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
    
    def archerHide(self):
        print(f"{self.name} quickly hides in foliage")

class KatsuneFox(Archer): # Gets access to Archer which has access to User. Multiple Inheritance
    pass

wizard1 = Wizard('Greg', 'Lightning')
archer1 = Archer('Alice', 'Telekinesis')
katsune1 = KatsuneFox('Vecna', 'Morph')

wizard1.powerAttack()
archer1.powerAttack()
katsune1.archerHide()


playerList = [wizard1, archer1]
for i in playerList:
    i.powerAttack()

