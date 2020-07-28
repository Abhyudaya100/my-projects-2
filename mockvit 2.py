N = int(input())
numbers = []
bit_score = []
result = 0
even_bit_score = []
odd_bit_score = []
even_count = 0
odd_count = 0
numbers = input().split(" ")
if N <= 500:
    for number in numbers:
        if len(number) == 3 and len(numbers) == N:
            largest_digit = max(int(d) for d in str(number))
            smallest_digit = min(int(d) for d in str(number))
            result = str(largest_digit * 11 + smallest_digit * 7)
            if len(result)<3:
                bit_score.append(str(result))
            else:
                bit_score.append(str(result[-2:]))
for i in range(0,len(bit_score),2):
    even_bit_score.append(bit_score[i])

for i in range(1,len(bit_score),2):
    odd_bit_score.append(bit_score[i])

for i in range(len(even_bit_score)):
    for j in range(len(even_bit_score)):
        if i == j:
            break
        else:
            if even_bit_score[i][0] == even_bit_score[j][0]:
                even_count += 1

for i in range(len(odd_bit_score)):
    for j in range(len(odd_bit_score)):
        if i == j:
            break
        else:
            if odd_bit_score[i][0] == odd_bit_score[j][0]:
                odd_count += 1
if odd_count >2:
    odd_count = 2

print(even_count + odd_count)