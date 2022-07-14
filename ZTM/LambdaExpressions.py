myList = [1,2,3,4,5,6,7]

def multiplyBy2(li):
    return li * 2

print(list(map(lambda item: item*2, myList))) # lambda is a single use function 
print(list(filter(lambda item: item % 2 != 0, myList)))


