
def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

start_number=int(input("Countdown from: "))
count_down(start_number)