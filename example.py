# example.py

def add3(a, b, c):
  return a + b + c
  
  
#test function here

def test_add3():
  assert add3(1, 2, 3) == 6
  assert add3(5, 5, 5,) == 15
  assert add3("EA", "Z", "Y") == "EAZY"
