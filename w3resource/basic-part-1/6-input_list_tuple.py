values = input("Enter some comma separated numbers: ")
csv = values.split()
print(csv)
l = list(csv)
t = tuple(csv)
print("List: ", l)
print("Tuple: ", t)

tt = tuple(*l, )
print(tt)
print(type(tt))
