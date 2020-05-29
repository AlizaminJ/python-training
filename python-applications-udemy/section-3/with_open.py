myfile = open("example.txt", "w")
myfile.write("coffee")
myfile.close()



# to skip .close() every time use with
#  'with' closes the file even a block between open and close gives error
with open("example.txt",  "w") as myfile:
    myfile.write("tea")

myfile = open("example.txt")
content = myfile.read()
print(content)
