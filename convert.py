import numpy as np

def c2f(c):
    f = (c * 9 / 5) + 32
    return round(f, 3)

def f2c(f): 
    c = (f - 32) * 5 / 9
    return round(c, 3)

#temperture
    
def kg2p(kg):
    p = kg * 2.2046
    return round(p, 3)

def p2kg(p):
    kg = p * 0.4535
    return round(kg, 3)

def o2kg(o):
    kg = 0.0283 * o
    return round(kg, 3)

def kg2o(kg):
    o = kg *35.2740
    return round(o, 3)

#weight

def M2m(M):
    m = M * 0.0006214
    return round(m, 4)

def M2i(M):
    i = M * 39.3700787
    return round(i, 3)

def M2f(M):
    f = M * 3.2808399
    return round(f, 3)

def m2M(m):
    M = m / 0.0006214
    return round(M, 3)

def i2M(i):
    M = i / 39.3700787
    return round(M, 3)

def f2M(f):
    M = f / 3.2808399
    return round(M, 3)

# length

def uc(ch1, ch2, num):


    if ch1 == "c" and ch2 =='f':
        cnum = c2f(num)
        print("{}C = {}F".format(num, cnum))
        return cnum

    elif ch1 == "f" and ch2 =='c':
        cnum = f2c(num)
        print("{}F = {}C".format(num, cnum))
        return cnum

    elif ch1 == "kg" and ch2 =='pound':
        cnum = kg2p(num)
        print("{}kg = {}pounds".format(num, cnum))
        return cnum

    elif ch1 == "pound" and ch2 =='kg':
        cnum = p2kg(num)
        print("{}pounds = {}kg".format(num, cnum))
        return cnum

    elif ch1 == "ounce" and ch2 =='kg':
        cnum = o2kg(num)
        print("{}ounces = {}kg".format(num, cnum))
        return cnum

    elif ch1 == "kg" and ch2 =='ounce':
        cnum = kg2o(num)
        print("{}kg = {}ounces".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='mile':
        cnum = M2m(num)
        print("{}M = {}miles".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='inch':
        cnum = M2i(num)
        print("{}M = {}inches".format(num, cnum))
        return cnum

    elif ch1 == "meter" and ch2 =='foot':
        cnum = M2f(num)
        print("{}M = {}feet".format(num, cnum))
        return cnum

    elif ch1 == "mile" and ch2 =='meter':
        cnum = m2M(num)
        print("{}miles = {}M".format(num, cnum))
        return cnum

    elif ch1 == "inch" and ch2 =='meter':
        cnum = i2M(num)
        print("{}inches = {}M".format(num, cnum))
        return cnum

    elif ch1 == "foot" and ch2 =='meter':
        cnum = f2M(num)
        print("{}feet = {}M".format(num, cnum))
        return cnum

    else:
        print("plesas input correct unit name")
        return "unit name incorrect"