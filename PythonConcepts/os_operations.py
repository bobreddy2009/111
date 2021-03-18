import os
from datetime import datetime
cwd = os.getcwd()
home_dir = 'C:/Users/avane/Documents/dummy'
os.chdir(home_dir)
#for i in range(2,51):
#    new_dir = f"d{i}"
#    os.mkdir(new_dir)
# for i in range(2,51):
#     new_dir = f"d{i}"
#     os.rmdir(new_dir)
# for i in range(1,5):
#     new_dir = f"d{i}"
#     os.mkdir(new_dir)
#     my_dir = new_dir
#     os.chdir(my_dir)
#DON'T use removedirs and rmdir unless ur in a dummy directory and u know what u are doing! NEVER USE REMOVEDIRS!!!!!!!!!!!!!!!!!!!!!!!!!
os.chdir(home_dir)
#print(os.listdir())
#os.rename('abc.txt','xyz')
print(os.listdir())
"""for file in os.listdir():
    if os.path.isdir(file):
        print(f"{file} is a Directory")
    if os.path.isfile(file):
        print(f"{file} is a file")
    mod_time = os.stat(file).st_mtime
    print(datetime.fromtimestamp(mod_time))
    print(os.stat(file).st_size)"""
def five_files():
    for i in range(1,6):
        file_name = f"abc{i}"
        with open(file_name,'w') as f:
            pass
#five_files()
def rename_abc():
    for file in os.listdir():
        if file.startswith('xyz') and os.path.isfile(file) and os.stat(file).st_size > 0:
            print(file)
            new_file_name = file.replace('xyz','pqr')
            print(new_file_name)
            os.rename(file,new_file_name)
rename_abc()

