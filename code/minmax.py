lt = [1,4,6,2,5,100,8,20,500,0]
min_val = max_val = lt[0]
count = 0


for i in lt:
    if i < min_val:
        min_val = i
    elif i > max_val:
        max_val = i
for i in lt:
    count += i
print(f'{max_val}\n{min_val}\n{count/(len(lt))}')


even = []
odd = []
for i in range(101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'{even}\n{odd}')
        
