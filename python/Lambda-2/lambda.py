add = lambda x,y: x +y
print(add(2,3))


num = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, num))
print(squared)

num = [ 1, 2, 3,4,5,6]
res = list(filter(lambda x: x %2 == 0, num))
print(res)
