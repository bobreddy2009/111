x = 10
print(id(x))
def outer_func():
    x = 20
    print(f"{x}: outer")
    def inner_func():
        nonlocal x
        print(f"{x}: inner")
        x += 10
        print(f"{x}:inner2")
    inner_func()
    print(f"outer_func() done")
    print(f"{x}: outer2")
outer_func()
print(x)
print(id(x))