string = input("Enter a string:")
strlen = len(string)
cols = strlen * 2 -1

for index in range(1,strlen + 1):
    print("%*c%*s"%(index,string[index-1],cols - index *2,"",string[index-1] if index != strlen else char(0)))

for index in range(1, strlen + 1):
    print("%*c%*s" % (index, string[index - 1], cols - index * 2, "", string[index - 1] if index != strlen else char(0)))