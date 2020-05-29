text = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

for i in text.split():
    if i[0].isupper():
        if i[0] == "I":
            print(i, end=" ")
        else:
            print("\n", i, end=" ")
    else:
        print(i, end=" ")

print("")
print("")

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
