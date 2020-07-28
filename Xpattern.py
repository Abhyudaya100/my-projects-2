#program to print string in x pattern
string = input("Enter the string:")
strlen = len(string)
cols = 2 * strlen - 1
for index in range(1,strlen):
    print((index-1)*" ",string[index-1], " " * (cols -(index*2)),string[index-1],sep = "")
print(" "* index, string[index],sep="")
for index in range(strlen-1,0,-1):
    print((index-1)*" ",string[index-1], " " * (cols -(index*2)),string[index-1],sep = "")
print(" "* index, string[index],sep="")