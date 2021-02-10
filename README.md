<<<<<<< HEAD
1. Написать генератор, который принимает параметры так же, как range.
может быть вызван так:
my_range(10) # stop
my_range(2, 10) # start, stop
my_range(2, 10, 2) # start, stop, step (edited) 

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

2. Написать свой декоратор, который выбирает рандомное приветствие для введенного имени
'Hello, <Name>', 'Welcome, <Name>','Greetings, <Name>!','Salutations, <Name>!','Good day, <Name>!', 'Yo, <Name>!'
3. Написать декоратор, который выводит время выполнения функции.
4. Написать логгер, который записывает в файл, какая функция и сколько выполнялась.
логгер - это декоратор, который принимает параметром имя файла.
=======
# lesson10
>>>>>>> 1d0d44ad1c4c6d5e12e0e0f185b6156ae812333c
