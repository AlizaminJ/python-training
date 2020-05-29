# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date
d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)
diff = d2-d1
print(diff.days)
