class Notes:
    __my_dict = {}
    def add(self,key,value):
        self.__my_dict[key] = value
    def get(self,key):
        if key in self.__my_dict:
            return self.__my_dict.get(key)
        else:
            return "Value not found"
z1 = Notes()
z1.add(key='country',value='USA')
z1.add(key='timezone', value='PST')
print(z1.get(key='state'))
print(z1.get(key='timezone'))