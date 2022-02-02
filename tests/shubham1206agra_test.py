n=int(input("Enter no of elements you want in the list"))
l=list()
for i in range(n):
    b=int(input("enter element,a number"))
    l=l.append(b)
length=len(l)
maximum_element=max(l)
minimum_element=min(l)
