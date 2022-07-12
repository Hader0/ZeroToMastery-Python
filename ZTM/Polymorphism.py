class User():
    def __init__(self, email):
        self.email = email
        
    def signIn(self):
        print("Logged in")

# Subclasses of Class User
class Wizard(User): # By passing the parent class, we're able to use the children functions
    def __init__(self, name, power, email):
        super().__init__(email) # Gives the function within the subclass access to the parent class function
        self.name = name
        self.power = power

    def powerAttack(self):
        print(f'"Boom" occured from {self.name}\'s {self.power}')

class Archer(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
        

    def powerAttack(self):
        print(f'"WHAM" occured from {self.name}\'s {self.power}')

wizard1 = Wizard('Greg', 'Lightning', 'wizard1@gmail.com')
archer1 = Archer('Alice', 'Telekinesis', 'archer1@gmail.com')

wizard1.powerAttack()
archer1.powerAttack()


playerList = [wizard1, archer1]
for i in playerList:
    i.powerAttack()

print(f"{wizard1.name}'s email: {wizard1.email}")
print(f"{archer1.name}'s email: {archer1.email}")