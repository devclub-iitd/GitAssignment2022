import time
n=10
m=10

def fx(n,a):
    for t in range(n):
        
        return(str(" "+'-'*n**2+' ' + '\\'*(m-a)))
        

def transition(a,stg,t):
    for b in range(a):
        print(str(stg) , end='')
        time.sleep(t)

        



for a in range(m):
    time.sleep(0.2)
    transition(a ,' ',0.05) 
    l=a**2
    transition(l,'+',0.005)  
    print(fx(n,a)) 
    print('')

while True:   
    fd=input('Is The Test Working? <y/n>: ')
    if fd=='y':
        print('ok')
        print('....~....')
        break

    if fd=='n':
        for a in range(5):
            print(' '*a + '*'*a)
        print('....~....')
        break  

    if fd=='exit':
        print('....~....')
        break

    else:
        print('enter <y/n> (or) exit')  
