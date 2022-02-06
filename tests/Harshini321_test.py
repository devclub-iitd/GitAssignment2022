def prime(n):
    #calculates no of prime numbers between [1,n]
    #including n
    sum=0
    for num in range(2,n+1):
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            sum=sum+1
    return sum

def test_prime():
    assert prime(100)==25, "oops, wrong ans"
test_prime()
