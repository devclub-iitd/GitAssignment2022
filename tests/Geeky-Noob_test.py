import numpy as np

def power(x,n):
    return(x*(power(x,n-1)))

def intro(a):
    return ('Hi everyone! My name is '+ a)

def test_len():
    assert len([1,2,3,4]) == 4

def test_numpy():
    assert np.sum([1,2,3,4]) == 10