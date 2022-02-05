import copy

def power(P):

    n = len(P)
    L = [[]]                     
      
    for i in range (0 , n):
        Q = copy.deepcopy(L)
        for j in range (0 , len(Q)):
            Q[j].append(P[i])
            L.append(Q[j])
    return L
  
print(power([1,2,3]))
