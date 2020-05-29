# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def func():
    n = int(input("Enter integer: "))
    n1 = int("%s" % n)
    n2 = int("%s%s" % (n, n))
    n3 = int("%s%s%s" % (n, n, n))
    return (n1 + n2 + n3)


print(func())
