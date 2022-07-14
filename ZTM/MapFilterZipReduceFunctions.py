# map() Function
myList = [2,4,6]

def multiplyBy2(li):
    return li * 2

print(list(map(multiplyBy2, [2,4,6,8]))) # map() is a shorter way of getting a result that would take several more lines of code

print(list(map(multiplyBy2, myList))) # Will use 'myList' as the input for the function

print(myList) # The list remains unaffected 


# filter() Function
def checkOdd(item):
    return item % 2 != 0   # If the remainder doesn't equal 0, which returns True, the item is odd

myList2 = [1,2,3,4,5]

print(list(filter(checkOdd, [2,4,5,9])))

print(list(filter(checkOdd, myList2)))


# zip() Function
myList3 = [10,20,30,40,50]

print(list(zip(myList, myList2, myList3))) # Combines the first index item of each list together 

# reduce() Fuction
from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, myList3, 0))