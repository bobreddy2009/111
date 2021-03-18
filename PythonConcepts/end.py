import re
search_string = """Hi, My name is Avaneesh. I like to see trending stuff. did you know steel can bend, its bends when 
                exposed to tempraterses above 100 degrees farenhiet, I have many friends """
my_string = r"\w+end\w+"
pattern = re.compile(my_string)
match = pattern.findall(search_string)
for word in match:
    print(word)
