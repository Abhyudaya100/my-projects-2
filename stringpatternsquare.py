'''
Enter a string :abhyudaya
abhyudayaabhyudaya
abhyuday  abhyuday
abhyuda    abhyuda
abhyud      abhyud
abhyu        abhyu
abhy          abhy
abh            abh
ab              ab
a                a
a                a
ab              ab
abh            abh
abhy          abhy
abhyu        abhyu
abhyud      abhyud
abhyuda    abhyuda
abhyuday  abhyuday
abhyudayaabhyudaya

'''

string = input("Enter a string :")
strlen = len(string)
for index in range(strlen):
    print(string[0:strlen-index] + " " * index * 2 + string[0:strlen-index])
    index +=1
for index in range(strlen):
    print(string[0:index+1] + " " * (strlen-index-1) * 2 + string[0:index+1])
    index +=1