#Merging Text Files (Practice)
#Here is another tricky exercise.
#1. Download and put into a folder the three text files attached in this lecture. The first text file contains the text Content1 ; the second file contains Content2 ; and the third file contains Content3 .

#2. You should create a Python script that generates a new text file, which should contain the content of all three text files. The generated file should have this content:
#Content1 
#Content2 
#Content3 

#In other words, your Python script should merge the three text files. 

#3. The name of the output file should be the current timestamp. Example: 2017-11-01-13-57-39-170965.txt 
#You have some tips in the next lecture and the solution is in the lecture after that.

import glob2
from datetime import datetime

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:       
        with open(filename, "r") as f:
            file.write(f.read() + "\n")