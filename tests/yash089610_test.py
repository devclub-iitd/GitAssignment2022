import random

def game():
    while True:
        num=random.randint(1,20)
        a=1
        con=None
        print("Guess the number between 1 to 20")
        while a<6:
            x=int(input(f"Guess {a}: "))
            if x==num:
                  print("You won")
                  return False
                  break
            elif num in range(x,x+2) or num in range(x,x-2,-1):
                print("You are close")
            elif x<num:
                  print("You entered a smaller number")
            elif x>num:
                  print("You entered a bigger number")
            a+=1
            if a==6:
                  print("You lost")
                  con=input("Try Again?(y/n)")
            if con=="n" or con=="no":
                  return False
                  break
            else:
                  continue
game()