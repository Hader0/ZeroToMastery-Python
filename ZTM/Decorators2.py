def myDecorator(func):
    def wrapFunction(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrapFunction

@myDecorator
def hello(greeting='Hi', emoji=':)'):
    print(greeting, emoji)

hello('Seeya')
hello() # Prints using default parameters 

###
from time import time
def performance(func):
    def wrapperFunc(*args, **kwargs):
        tStart = time()
        result = func(*args, **kwargs)
        tFinish = time()
        print(f'Time: {tFinish-tStart} Seconds')
        return result
    return wrapperFunc()

@performance
def performanceTest():
    for i in range(1000000):
        i*5.79