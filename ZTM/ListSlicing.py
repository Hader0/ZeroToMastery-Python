listOne = [1,2,3,4,5]

# Copy to a new list without a change affecting the original
listTwo = listOne[:]

listTwo[0] = 5

print(listOne)
print(listTwo)