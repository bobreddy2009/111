def simplify(fraction):
    numbers = fraction.split('/')
    numerator = int(numbers[0])
    denometer = int(numbers[1])
    numerstor_factors = []
    denometer_factors = []
    common_factors = []
    for number in range(1,numerator+1):
        if numerator % number == 0:
            numerstor_factors.append(number)
    for number in range(1,denometer+1):
        if denometer % number == 0:
            denometer_factors.append(number)
    common_factors = [factor for factor in numerstor_factors if factor in denometer_factors]
    divider = max(common_factors)
    numerator = int(numerator/divider)
    denometer = int(denometer/divider)
    if denometer == 1.0:
        print(numerator)
    else:
        print(f"{numerator}/{denometer}")
simplify("7/10")
#[DC]a[4-7]
#[58][58][58]-\d\d\d-\d\d\d
#om.