num = [10, 7, 8, 11, 6, 5]
count = 0
for i in num:
    for j in range(1, len(num) + 1):
        if num[j] < i:
            num.insert(count, i)