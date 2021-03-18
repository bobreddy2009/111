import os
os_home = os.environ.get('USERPROFILE')
home_dir = os_home + "/Documents/dummy"
print(home_dir)
os.chdir(home_dir)
sizes = {}
sizes_list = []

for num in range(1,6):
    name = f"d{num}"
    print(name)
    #os.mkdir(f"d{num}")
    for num2 in range(1,6):
        file_name = f"{name}_f{num2}"
        final_file_name = os.path.join(home_dir,name,file_name)
        #print(final_file_name)
        #with open(final_file_name, 'w') as f:
        #    pass
        sizes[os.stat(final_file_name).st_size] = final_file_name
        sizes_list.append(os.stat(final_file_name).st_size)
sizes_list.sort()
#print(sizes_list)
#print(sizes)
for size in sizes_list:
    print(size,sizes.get(size))



