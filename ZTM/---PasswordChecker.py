username = input("Enter a Username: ")
password = input("Enter a Password: ")

hiddenPassword = '*' * len(password)

print(f'Password {hiddenPassword} is {len(password)} letters long!')
