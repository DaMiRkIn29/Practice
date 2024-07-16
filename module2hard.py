import random

first_num = random.randint(3,20)
print(first_num)

couples = []
result = ""

for i in range(1, first_num):
    for j in range(i, first_num):
        if first_num % (i + j) == 0 and i != j:
            couples.append([i, j])
            result += str(i) + str(j)
            
print(couples)
print(result)