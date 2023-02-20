import re

regex = r'^1?\s?(\d{3}|\(\d{3}\))-?\s?\d{3}-?\s?\d{4}$'

num = input('Enter US phone number to validate ')

match = re.match(regex, num)

print(bool(match))
