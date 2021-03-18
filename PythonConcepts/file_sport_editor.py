data = ""
letter_count = 0
with open(file = "file_sport.txt") as f:
    for line in f:
        spaces = line.count(" ")
        words = spaces + 1
        letter_count += words
        data += line
        if letter_count >= 100:
            letter_count = 0
            data += "\n"
            data += "edited by: Avaneesh Dammanagari"
            data += "\n"
with open(file = "file_sports_edited.txt", mode="w") as f:
    f.write(data)