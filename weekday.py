day = int(input("Enter the day number from 1 to 7 :"))

if day == 1:
    print("its monday, get ready for work")
elif day in [2,3,4]:
    print("its still a weekday")
elif day == 5:
    print("Its friday, get ready for weekend")
elif day in [6,7]:
    print("enjoy the weekend")
else:
    print("invalid day number")