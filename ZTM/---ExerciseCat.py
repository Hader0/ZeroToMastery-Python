#Given the below class:
from email.policy import compat32


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Bruce', 12)
cat2 = Cat('Sprinkles', 2)
cat3 = Cat('Little One', 5)


# 2 Create a function that finds the oldest cat
catList = [cat1, cat2, cat3]
catAges = []

def eldestCat(): # Function to find and return eldest cat age
    i = 0
    for catList[i] in catList:
        catAges.append(catList[i].age)
    return(max(catAges))



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {eldestCat()} years old')

