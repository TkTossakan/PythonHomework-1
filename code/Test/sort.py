num = [3, 5, 4, 1, 2]
j = 0
temp = 0
for i in range(1, len(num)):
    temp = num[i]
    j = i - 1
    while j >= 0 and num[j] > temp:
        num[j + 1] = num[j]
        j -= 1
    num[j + 1] = temp
print(num)
