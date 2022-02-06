#Sorting on the basis of length of string
#Use of sorting key
print("Enter space separated strings")
li=list(map(str,input().split()))
li.sort(key= len)
for i in li:
    print(i,end=" ")

#if two elements are of same length, the one entered first will be printed first