# Splits at space
text = 'geeks for geeks'
print(text.split())

# Splits at ','
word = 'geeks, for, geeks'
print(word.split(', '))

# Splitting at ':'
word = 'geeks:for:geeks'
print(word.split(':'))

# Splitting at 3
word = 'CatBatSatFatOr'
print([word[i:i+3] for i in range(0, len(word), 3)])

# Getting extension, e.g. "abc.java"
filename = input("Filename: ")
ext = filename.split(".")
print(ext[-1])
