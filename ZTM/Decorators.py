def addition(num1,num2):
    return num1 + num2

num3 = 2
num4 = 4

addition2 = addition # Assigning addition2 as addition()
del addition # Deleting addition() function

print(addition2(num3, num4)) # Still prints because addition2 didnt become a copy of addition(),
                             # it became a seperate variable holding that function

# Using a function to call a function

def hello(func):
    func()

def greet():
    print("Hello, there!")

a = hello(greet)

