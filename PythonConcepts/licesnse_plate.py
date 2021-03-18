def licesne_fix(plate,group):
    plate = plate.upper()
    plate_reversed = []
    for i in plate:
        plate_reversed.insert(0,i)
    output = []
    for index,letter in enumerate(plate_reversed):
        output.insert(0, letter)
        if (index + 1) % group == 0:
            output.insert(0, "-")
    if output[0] == '-':
        output.remove('-')
    print("".join(output))
licesne_fix("juhnujhbhjbjhbhjbnjuhnujhbhjbjhbhjbnjuhnujhbhjbjhbhjbnjuhnujhbhjbjhbhjbn",10)