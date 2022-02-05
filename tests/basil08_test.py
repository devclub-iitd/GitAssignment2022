import numpy as np

def test_len():
  assert len([x**2 for x in range(100)]) == 100

def test_sum():
  assert sum([2*x-1 for x in range(1, 99)]) ==  99**2
