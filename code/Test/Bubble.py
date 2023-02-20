import random as rd


def did_swarp(a, b):
    return a > b


num = []

for i in range(15):
    num.append(rd.randint(0, 100))


def ssort(num):

    count = 0
    didswarp = True
    to_do = 0

    while True:

        didswarp = did_swarp(num[count], num[count + 1])

        if didswarp:
            num[count], num[count + 1] = num[count + 1], num[count]

        count += 1
        if count == len(num) - 1:
            count = 0

        to_do += 1
        if to_do == len(num) ** 2:
            break

    return num


print(ssort(num))
