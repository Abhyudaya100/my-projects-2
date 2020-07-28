string = input("enter a string :")
strlen = len(string)
for index in range(strlen,0,-1):
    print(" " * (strlen - index) + string[:index])