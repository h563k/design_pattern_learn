item = ["hello"]
items = [item] * 3  # 乘 3 之后得到的是一个 3行, 1列的二维数组, 而不是个1行3列的数组
print(items)  # [['hello'], ['hello'], ['hello']]
items_1 = item * 3  # 乘 3 之后得到一个 1行, 3列的一维数组
print(items_1)  # ['hello', 'hello', 'hello']
items[0][0] = "world"
print(items)  # [['world'], ['world'], ['world']]
items_1[0] = "world"
print(items_1)  # ['world', 'hello', 'hello']
# print(items[0][1]) # IndexError: list index out of range
# print(items[0][2]) # IndexError: list index out of range
print(items[0][0]) # world
print(items[1][0]) # world
print(items[2][0]) # world