import re
search_string = "jacky36@gmail.com"
my_string = r"[\w\.\-\_]+@[a-zA-z]+.(edu|com)"
pattern = re.compile(my_string)
match = pattern.match(search_string)
if match:
    print(f"{match.group()} IS A VALID EMAIL. :)")
else:
    print("NOT A VALID EMAIL!! :(")