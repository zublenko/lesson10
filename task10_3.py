def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        return 'Время выполнения: {} секунд.'.format(end - start)
    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


print(fetch_webpage())
