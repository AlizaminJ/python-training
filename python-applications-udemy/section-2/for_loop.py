mylist = [1, 2, 3, 4, 5] 

for i in mylist:
    print (i)

print("")
for i in (1, 2, 3):
    print(i + 1)

print("")
mylist = ["Trickier"]
for item in mylist:
    print(item)

print("")
mylist = ["Terribly Tricky", "Awesome"] 
for word in mylist:
    for letter in word[-6:]:
        print(letter)

print("")
mylist = [1, 2, 3, 4, 5] 
for i in mylist:
    if i>2:
        print(i)
    
print("")
file = open("fruits.txt")
fruit = file.read()
file.close()
fruit = fruit.splitlines()
for f in fruit:
    print(len(f))

# Another way is to use readlines() :
print("")
file = open("fruits.txt")
content = file.readlines()
content = [line.strip() for line in content]
file.close()
for i in content:
    print(len(i))
