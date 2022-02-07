def factorial(n):
    count = 0
    pd = 1
    while(True):
        if(count==n):
            break
        else:
            count+=1
            pd*= count
    return pd

def test_factorial():
    assert factorial(5) == 120