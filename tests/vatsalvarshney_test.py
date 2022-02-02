def listsum(l1,l2):
    l=[]
    for i in range(0,len(l1)):
        l.append(l1[i]+l2[i])
    return l

def test_1():
    assert listsum([8,3,4,0],[2,4,6,1])==[10,7,10,1]

def test_2():
    assert listsum([9,4,8],[3,7,3])==[12,11,11]