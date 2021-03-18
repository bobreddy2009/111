import math
def LPT_OR_RPT(num):
    lpt_prime = True
    rpt_prime = True
    num1 = num
    num2 = num
    for digit in range(len(str(num)) - 1):
        if rpt_prime == False:
            break
        num1 = str(num1)[0:-1]
        y = int(math.sqrt(int(num1))) + 1
        for i in range(2, y):
            if int(num1) % i == 0:
                rpt_prime = False
                break
    for digit in range(len(str(num)) - 1):
        if lpt_prime == False:
            break
        num2 = str(num2)[1:]
        y = int(math.sqrt(int(num2))) + 1
        for i in range(2, y):
            if int(num2) % i == 0:
                lpt_prime = False
                break
    if '0' in str(num):
        print('the number is not LPT or RPT')
    elif rpt_prime == True and lpt_prime == True:
        print('the number is both lpt and rpt')
    elif rpt_prime == True and lpt_prime != True:
        print('The number is only RPT prime')
    elif lpt_prime == True and rpt_prime != True:
        print('the number is  only LPT prime')
    else:
        print('the number is not LPT or RPT')


LPT_OR_RPT(3137)
