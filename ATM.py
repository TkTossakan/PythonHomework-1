money = input('Please enter amount : ')
for i in (1000,500,100):
    output = int(money)/i
    money = int(money) - int(output)*i
    print(f'{i} : {int(output)}')