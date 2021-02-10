def generate_range(stop, start=2, step=2):
    i=start
    while i<stop:
        yield i
        i+=step



print(list(generate_range(9)))
