count = 0
while count<3:
    try:
        num = int(input("Enter an integer:"))
        break
    except ValueError as error:
        print("please enter numbers only")
    count+=1
else:
    print("3 attempts are over")
    exit(0)
assert (num>0), "Invalid Input"
if num%2 == 0:
    print("Even")
else:
    print("odd")