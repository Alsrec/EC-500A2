# example.py
import numpy as np

def add3(a, b, c):
  return a + b + c

def numpyaround(a, b):
  returen np.around(a, b)
  
  
  
#test function here

def test_add3():
  assert add3(1, 2, 3) == 6
  assert add3(5, 5, 5,) == 15
  assert add3("EA", "Z", "Y") == "EAZY"

  def test_numpyaround:
    assert numpyaround(1.222, 1) == 1.2
