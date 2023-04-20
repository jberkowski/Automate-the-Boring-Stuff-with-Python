"""Searches for the USA-formatted phone number (e.g. 123-456-7890) in a string 
using regular expression."""

import re

# Create regular expression matching out number format.
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# Search for our Regex in a string containing one number.
mo1 = phoneNumRegex.search('My phone number is 123-123-7368.')

# Display phone number found.
print('Phone number found: ' + mo1.group())

# Separately group area code and main number with parentheses.
groupNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = groupNumRegex.search('My number is 432-109-8765')

# Show each group.
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# Show tuple containing all the groups.
print(mo.groups())