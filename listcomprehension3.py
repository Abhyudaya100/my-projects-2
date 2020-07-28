list1 = [1,2,3,4,5,6]
evalist = [element ** 2 if element% 2 ==1 else element ** 3 for element in list1]
print(*evalist)

