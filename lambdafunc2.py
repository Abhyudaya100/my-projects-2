convert = lambda element:int(element) if element.find(".")==-1 else float(element)
numlist = [convert(element) for element in input("Enter values :").split()]
print(*numlist)