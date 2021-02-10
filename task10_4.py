def time_webpage(function):
    import time

    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        with open("/root/python/lesson10/log_file", "a+") as log:
            log.write(f'Name of func: {function.__name__}\nLead time: {str(time.time() - start_time)}\n----------\n')
        return res

    return wrapped


@time_webpage
def do_something(x):
    return x**55


do_something(9)
