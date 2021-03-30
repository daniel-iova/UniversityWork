from random import *

for it in range(1, 11):
    s = "input" + str(it) + ".in"
    outfile = open(s, "w")
    n = randint(1, 70)
    n = it
    x = randint(0, 100)
    input_arr = []
    print(n, file = outfile)
    while (x != randint(20, 100)):
        a = randint(0, n-1)
        b = randint(0, n-1)
        if (a != b):
            input_arr.append((a, b))
        x = randint(0, 100)
    input_arr = list(dict.fromkeys(input_arr))
    input_arr.sort()
    res = [tuple(reversed(i)) for i in input_arr]
    final = []
    for i in input_arr:
        if i in res:
            input_arr.pop(input_arr.index(i))
    for i in input_arr:
        print (f"{i[0]} {i[1]}", file=outfile)