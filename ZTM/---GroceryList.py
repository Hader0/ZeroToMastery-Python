groceries = []
i = 0

while i == 0:
    item = input("What grocery item would you like added? ")
    item = item.capitalize()
    groceries.append(item)
    print(item)
    decision = input("Would you like to add another item? (Y/N): ")
    if "y" in decision:
        print(f'Groceries Include: {item}')
    else:
        print('Have a good day!')
        i+=1