def float_range(start = 0,stop = 0, step = 1):
    yield start
    while True:
        if start + step > stop:
            break
        start+=step
        yield start

y = float_range(0.2,1.3,0.3)
for i in y:
    print(i)