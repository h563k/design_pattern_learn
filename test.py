def func(x):
    x = yield x
    x = yield x

m = func(3)
for x in m:
    print(x, end='') # 3None