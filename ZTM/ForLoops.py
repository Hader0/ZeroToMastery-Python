for i in 'hello':
    print('hello')

for i in [1,2,3,4,5]:
    for ii in ['a','b','c','d','e']:
        print(i, ii)

# Iterate over Dictionary's
podium = {
    'first-place': 'Anakin',
    'second-place': 'Luke',
    'third-place': 'Obi-Wan'
}

for i in podium:
    print(i) # Prints the variable in the dictionary

for i in podium.values():
    print(i) # Prints the values in the dictionary

for i in podium.items():
    print(i) # Prints both keys and values in the dictionary

for i in podium.keys():
    print(i) # Prints the keys in the dictionary


# Allocating the keys and values as variables
for key, value in podium.items():
    print(key)
    print(value)


# Count items in list
listOne = [1,2,3,4,5]
count = 0
for i in listOne:
    count+=1
    print(count)

print(count) # 'Count' variable has now kept the value

for i in range(0,10):
    print(i)

for i in range(10,0,-1):
    print(i) # Start, Stop, Stepover from 10 to 1

for i in range(0,3):
    print(list(range(10 + 1)))