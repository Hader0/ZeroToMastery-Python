evens = []

def highestEven(evenNums):
    for i in evenNums:
        if i % 2 == 0:
            evens.append(i)
    return(max(evens))
    



print(highestEven([100,1,2,70,3,4,8,3000]))