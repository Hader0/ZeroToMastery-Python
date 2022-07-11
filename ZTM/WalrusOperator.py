stringOne = 'Boooooooo'

if ((n := len(stringOne)) > 3):
    print(f'The string {stringOne} is too long')
    print('Recommendation:')
    while ((n := len(stringOne)) > 3):
        stringOne = stringOne[:-1]

    print(f'Would you prefer "{stringOne}"?')

