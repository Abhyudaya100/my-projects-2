string = input("enter a string:")
x = len(string)
y=0
for char in string:
    if y<x:
        print(string[0:y + 1])
        y+=1