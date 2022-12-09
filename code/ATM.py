money = int(input('Please enter amount : '))
for i in (1000,500,100):
    print(f'{i} : {(money) // i}')
    money %= i