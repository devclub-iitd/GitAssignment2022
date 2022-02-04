def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def sum(x,y):
    return (x+y)

def test_sum():
    assert sum(4,6) == 10
    
def len(P):
    return len(P)

def test_len():
    assert len([1,2,3,4,5,6,7]) == 7


def power(x,y):
    return x**y

def test_power():
    assert power(2,3) == 8


def remainder(a,b):
    return a%b

def test_remainder():
    assert remainder(7,3) == 1
 