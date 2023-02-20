money = int(input())
for i in (1000, 500, 100, 50, 20, 10, 1):
    print(f"{money // i} ", end="")
    money %= i
