# dateDetection.py - regular expression that can detect dates in DD/MM/YYY format. Also verifies if the date is correct. File has to be names "datefile.txt" and be in the same location as this script.


import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

# Read text from file:
file = open("datefile.txt", "r")
text = file.read()

# Find matches in text:
matches = []
for groups in dateRegex.findall(text):
    matches.append(groups)

# Verify dates:
verified = []
for date in matches:
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if day > 31 or month > 12 or year > 2999: # Verify maximum values 
        continue

    if month in (4, 6, 9, 11) and day > 30: # Verify months that have only 30 days
        continue

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # Check if year is a leap year
        leapyear = True
    else:
        leapyear = False

    if month == 2 and leapyear and day > 29: # Check how many days can February have.
        continue
    elif month == 2 and leapyear == False and day > 28:
        continue

    verified_date = str(day)+"/"+str(month)+"/"+str(year)
    verified.append(verified_date)   


# Create a new file with results:
with open('dateResults.txt', 'w') as f:
    f.write('\n'.join(verified))

