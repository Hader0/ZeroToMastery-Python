def funky(*args, **kwargs): # 'args' accepts any parameter
    print(kwargs)           # 'kwargs' takes dictionary declarations 
    return sum(args)

(funky(1,3,1,5, name='Hayden', age='20'))