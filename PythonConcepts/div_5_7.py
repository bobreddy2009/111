def div_5_or_7(x):
    output = []
    for i in range(1,x+1):
        if i % 35 == 0:
            pass
        if i % 7 == 0 or i % 5 == 0:
            output.append(i)
    print(output)

print(div_5_or_7(50))
