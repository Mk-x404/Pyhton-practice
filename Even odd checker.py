# Program: Even or Odd Number Checker (with Loop)

i = 0
while True:
    user = int(input("Enter the desired number you wanna check: "))

    if user % 2 == 0:
        print(f"It’s an even number: {user}")
    else:
        print(f"It’s an odd number: {user}")

    user1 = input("Type 'Y' to continue or 'N' to stop: ").upper()
    
    if user1 == "N":
        print("Exit!!")
        break
    elif user1 == "Y":
        continue
    else:
        print("Invalid input. Exiting for safety.")
        break
