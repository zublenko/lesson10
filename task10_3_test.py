'''def time_webpage(function):
    import time
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(time.time() - start_time)
        return res
    return wrapped


@time_webpage
def request_webpage():
    import requests
    webpage = requests.get('https://google.com')

#def func(first, second):
#   return int(first) * int(second)


request_webpage()
'''
