from convert import *
import pytest

def test_cm():
  # assert some right cases
  assert uc("c", "f", 12) == 53.6
  assert uc("f", "c", 50) == 10.0
  assert uc("kg", "pound", 10) == 22.046
  assert uc("pound", "kg", 100) == 43.45
  assert uc("kg", "ounce", 10) == 352.74
  assert uc("ounce", "kg", 100) == 2.83
  assert uc("meter", "mile", 1000) == 0.6214
  assert uc("meter", "inch", 10) == 393.701
  assert uc("meter", "foot", 10) == 32.808
  assert uc("mile", "meter", 1) == 1609.269
  assert uc("inch", "meter", 100) == 2.54
  assert uc("foot", "meter", 100) == 30.48
  assert uc("fot", "meter", 100) == "unit name incorrect"
 

  
