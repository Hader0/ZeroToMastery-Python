# A pure function should: - Always produce the same output
#                         - Not create sideaffects
def multiplyBy2(li):
    outputList = []
    for item in li:
        outputList.append(item*2)
    return outputList

(print(multiplyBy2([2,4,8,10])))