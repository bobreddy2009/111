list1=[1,2.1,3,4.3,5]
ints = filter(lambda a: type(a)==int,list1)
print(list(ints))