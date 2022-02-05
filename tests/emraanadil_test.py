
def count_down(start_number):
    

    current=start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

while True:
  try:
    num = int(input("Enter an integer number: "))
    break
  except ValueError:
      print("Please input integer only...")  
      continue
count_down(num)