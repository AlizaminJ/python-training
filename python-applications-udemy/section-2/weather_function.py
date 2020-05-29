# Weather function
def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(cel_to_fahr(10))

temperatures = [10, -20, 100]
for t in temperatures:
    print(cel_to_fahr(t))