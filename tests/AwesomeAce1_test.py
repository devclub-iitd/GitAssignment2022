def checkinput(a):
    if a in "YNyn":
        if a in "Yy":
            return True
        else:
            return False
    else:
        a = input("wrong input, only y/n")
        return checkinput(a)
        

print("Just some random code")

x = True
while x :
    a = int(input("Enter a number"))
    for _ in range(a):
        print("FOOL",end = " ")
    print()
    b = input("Do you wish to continue?Y/N")
    x = checkinput(b)