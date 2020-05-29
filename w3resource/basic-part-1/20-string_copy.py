# Write a Python program to get a string which is n (non-negative integer) copies of a given string.


def string(x, n):
    return n*x


print(string("foo", 2))


def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))
