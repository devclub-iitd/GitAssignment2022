def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
    assert inc(45) == 46


def sum(x,y):
    return (x+y)

def test_sum():
    assert sum(4,6) == 10
    assert sum(4,56) == 60


def power(x,y):
    return x**y

def test_power():
    assert power(2,3) == 8
    assert power(2,3) == 8


def remainder(a,b):
    return a%b

def test_remainder():
    assert remainder(7,3) == 1
    assert remainder(7,2) == 1
    assert remainder(10,2) == 0