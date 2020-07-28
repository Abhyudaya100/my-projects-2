x,y,z = input("Enter 3 values :").split()
x,y,z = int(x), int(y), int(z)
'''
if x>y:
    if x>z:
        print(x,"is greater")
    else:
        print(z,"is greater")
elif y>z:
    print(y,"is greater")
else:
    print(z,"is greater")
'''
print(max(x,y,z),"is greater")