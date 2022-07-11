from audioop import ratecv


class PlayerCharacter:
    def __init__(self, name, age, race, raceClass, yell): # 'Self' is used as a placeholder/reference 
        self.name = name                            # for something that hasnt been created yet.
        self.age = age 
        self.race = race
        self.raceClass = raceClass
        self.yell = yell

ageInput = input("What's your player's age? ")
nameInput = input("What's your player's name? ")
raceinput = input("What class would you like to choose?\n1. Orc\n2. Elf\n3. Human\n4. Vampire\nDecision: ")
raceClassInput = input("What class would you like to play?\n1. Mage\n2. Warrior\n3. Hunter\n4. Druid\nDecision: ")
playerPhrase = input("What would you like your players main phrase to be? ")
greeting = input("What would you like your greeting to be? ")

player1 = PlayerCharacter(nameInput, ageInput, raceinput, raceClassInput, playerPhrase)

# Another way of assigning
player1.greet = greeting
print(player1.greet)

print(f'Player Name: {player1.name}\nPlayer Age: {player1.age}\nPlayer Race: {player1.race}\nPlayer Class: {player1.raceClass}')

print(f'{player1.name}: "{player1.yell}"')
