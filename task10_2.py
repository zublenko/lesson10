import random


def random_greet(func):
    def wrapper(name):
        greet_list = ['Hello', 'Welcome', 'Greetings', 'Salutations','Good day', 'Yo']
        return '{}, {}!'.format(random.choice(greet_list), func(name))
    return wrapper


@random_greet
def name_func(name):
    return name


print(name_func('Vladimir'))
print(name_func('Vladimir'))
print(name_func('Vladimir'))
