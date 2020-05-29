# Files, Loops, Functions, and Conditionals (Practice)
# For this exercise, write the output in a text file instead of printing the output in the terminal.
# The text file content will look like this:
# Don't write any message in the text file when input is lower than -273.15.

# From previous exercise
temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    print(c_to_f(t))


# Solution 1
temp = open("temp_output.txt", "w")
for t in temperatures:
    if t > -273.15:
        temp.write(str(c_to_f(t))+"\n")
temp.close()

with open("temp_output.txt") as temp_file:
    content = temp_file.read()
    print(content)

# Solution 2
temperatures = [10,-20,-289,100]
 
def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")
 
writer(temperatures) #Here we're calling the function, otherwise no output will be generated

# Solution 3
temperatures = [10,-20,-289,100]
 
def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")
 
writer(temperatures, "temps.txt") #Here we're calling the function, otherwise no output will be generated