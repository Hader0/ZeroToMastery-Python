while True:
    try:
        age = int(input("Age: "))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please age higher than 0')
    else:
        break

def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError:
        print('Please only enter numbers')

sum('1', 2)