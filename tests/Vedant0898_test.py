def num_of_unique(arr):
    """Finds number of unique elements in an array"""
    return len(set(arr))

def calc_fib(n,A,B):
    """Calculates the nth fibonacci number where first num = A 
    and second num=B"""
    a = A
    b = B
    if n==1:
        return a
    elif n==2:
        return b
    else:
        for _ in range(n-2):
            a,b = b,a+b
        return b


def test_unique():
    assert num_of_unique([2,3,7,1,2,8,3,2,8,1,5]) == 6

def test_fib():
    assert calc_fib(10,1,2) == 89
