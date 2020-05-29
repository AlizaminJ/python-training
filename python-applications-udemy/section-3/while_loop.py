correct_password = "python4ever"
name = input("Enter your name: ")
surname = input("Enter your surname: ")

password = input("Enter your password:")

while password != correct_password:
    password = input ("wrong! try again: ")

message = "Hi %s %s, you are logged in!" % (name, surname)
print(message)