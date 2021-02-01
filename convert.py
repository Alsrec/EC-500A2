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