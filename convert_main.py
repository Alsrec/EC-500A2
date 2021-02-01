import convert as cv

print("whcih unit you want to convert?\nChoose from c f kg ounce pound meter mile inch foot\n")


ch1 = input("From?")
ch2 = input("To?")

num = input("Please input the specific value\n")
if str.isdigit(num) == False:
    print("Please input numbers!!")
    exit
num = float(num)
#print(num, type(num))

def uc(ch1, ch2, num):


    if ch1 == "c" and ch2 =='f':
        cnum = cv.c2f(num)
        print("{}C = {}F".format(num, cnum))
        return cnum

    elif ch1 == "f" and ch2 =='c':
        cnum = cv.f2c(num)
        print("{}F = {}C".format(num, cnum))
        return cnum

    elif ch1 == "kg" and ch2 =='pound':
        cnum = cv.kg2p(num)
        print("{}kg = {}pounds".format(num, cnum))
        return cnum

    elif ch1 == "pound" and ch2 =='kg':
        cnum = cv.p2kg(num)
        print("{}pounds = {}kg".format(num, cnum))
        return cnum

    elif ch1 == "ounce" and ch2 =='kg':
        cnum = cv.o2kg(num)
        print("{}ounces = {}kg".format(num, cnum))
        return cnum

    elif ch1 == "kg" and ch2 =='ounce':
        cnum = cv.kg2o(num)
        print("{}kg = {}ounces".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='mile':
        cnum = cv.M2m(num)
        print("{}M = {}miles".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='inch':
        cnum = cv.M2i(num)
        print("{}M = {}inches".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='foot':
        cnum = cv.M2f(num)
        print("{}M = {}feet".format(num, cnum))
        return cnum

    elif ch1 == "mile" and ch2 =='meter':
        cnum = cv.m2M(num)
        print("{}miles = {}M".format(num, cnum))
        return cnum

    elif ch1 == "inch" and ch2 =='meter':
        cnum = cv.i2M(num)
        print("{}inches = {}M".format(num, cnum))
        return cnum

    elif ch1 == "foot" and ch2 =='meter':
        cnum = cv.f2M(num)
        print("{}feet = {}M".format(num, cnum))
        return cnum

    else:
        print("plesas input correct unit name")
        return "unit name incorrect"

uc(ch1, ch2, num)