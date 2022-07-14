# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Greg',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(func):
    def wrapperFunc(*args, **kwargs):
        if args[0]['valid']:
            return func(*args, **kwargs)
        else:
            return print("User not valid")
    return wrapperFunc


@authenticated
def message_friends(user):
    print('Message has been sent')

message_friends(user1)
message_friends(user2)