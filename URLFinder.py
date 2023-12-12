# URLFinder.py - Finds http:// and https:// addresses within text file. File has to be names "webfile.txt" and be in the same location as this script.

import re

# Create URl regex:
URLRegex = re.compile(r'''(
    (http://|https://)      # beginning of an address
    (\S+)                   # rest of the address
    [a-zA-Z0-9]             # ending in a letter or number
)''', re.VERBOSE)

# Read text from file:
file = open("webfile.txt", "r")
text = file.read()

# Find matches in text:
matches = []
for groups in URLRegex.findall(text):
    matches.append(groups[0])

# Create a new file with results:
with open('URLresults.txt', 'w') as f:
    f.write('\n'.join(matches))