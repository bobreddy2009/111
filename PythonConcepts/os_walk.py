import os
os_home = os.environ.get('USERPROFILE')
home_dir = os_home + "/Documents/dummy"
print(home_dir)
os.chdir(home_dir)
file = 'my_file.txt'
#file_name = home_dir +'/' +  'd1' + '/'+ file - never use this use os.join(inputs)
file_name = os.path.join(home_dir,'d1',file)
with open(file_name,'w') as f:
    f.write('hello world')
current_dir = os.getcwd()
print(current_dir)
print(file_name)
f_path,f_name = os.path.split(file_name)
print(os.path.splitext(file_name))
print(os.path.isdir(f_path))
"""#for current_path,dirs,files in os.walk(home_dir):
#    print(current_path,dirs,files)
for i in os.listdir():
    #print(os.stat(i))
    #print(os.path.split(i))
    print(i)
#os_home = os.environ.get('USERPROFILE')
#for i in d1:
#    print(i, d1.get(i))
#print(os_home)"""