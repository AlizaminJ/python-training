# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

n = float(input("Enter number: "))


def difference(n):
    if n <= 17:
        x = 17-n
    else:
        x = 2*(abs(17-n)
    return (x)


print(difference(n))
