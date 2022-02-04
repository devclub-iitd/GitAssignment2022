import random
a=random.randint(1, 100)
b=int(input('enter a number between 1 and 100 to win this game'))
if(a==b):
        print('you win')
else:
        print('sorry,you lost')
        