import timeit
def dec_for_loops(function):
    def inner(x):
        l = timeit.default_timer()
        function(x)
        return l * 60
    return inner

@dec_for_loops
def loops(x):
    for i in range(x):
        for j in range(x):
            for l in range(x):
                print(" ")
print(loops(100))