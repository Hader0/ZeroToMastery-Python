setOne = {1,2,2,3,4,5,5} # This is a set where every iterable needs to be unique

print(setOne) # Prints only the unique items, not the duplicats 

setOne.add(6)
setOne.add(1)

print(setOne) # The '1' wasnt printed because it's a duplicate

# Turning a list into a set

listOne = [1,2,3,3,4,5,5]

set(listOne)

print(set(listOne))