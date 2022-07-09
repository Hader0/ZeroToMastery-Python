listMethod = [1,2,3,4,5]
print(listMethod)

# Add to list
listMethod.append(6) # Adds to end of list
print(listMethod)

listMethod.insert(6, 7) # Adds to the specified index
print(listMethod)

listExtension = [8,9,10]
listMethod.extend(listExtension) # Adds all elements of an iterable to the end of the list
print(listMethod)


# Remove from list
listMethod.pop(0) # Removes the specified index. Default .pop() removes last item
print(listMethod)

listPop = listMethod.pop(8) # Creates a new variable with only the index
print(listPop)

listMethod.remove(2) # Removes the value
print(listMethod)

listMethod.clear() # Clears the list
print(listMethod)


# Get Index of Value
listMethod = [1,2,3,4,5]

print(listMethod.index(4))

print(listMethod.index(5, 0, 6)) # The last two parameters determine where to start and stop looking for '5'