class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

personId = Person('Hayden', 20, 'Male')

personIdDisplay = print(f"Person Details\n----------------\nName: {personId.name}\nAge: {personId.age}\nGender: {personId.gender}")

class SuperList(list):
    def __len__(self):
        return 1000

superlist1 = SuperList()

nums = [5,4,3,2,1]

for i in nums: # Appends each iterable from nums into the Person Class
    superlist1.append(i)

print(superlist1[:]) # Prints the entire list
print(superlist1[0::2]) # Prints the entire list execpt for every 2
print(superlist1[::-1]) # Reverses the list