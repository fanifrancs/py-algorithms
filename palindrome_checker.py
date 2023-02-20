import re

regex = '[^A-Za-z0-9]'

def reverseString (str):
    return (str[::-1])

def palindrome(str):
    sanitized = re.sub(regex, '', str).lower()
    if sanitized == reverseString(sanitized):
        print(True)
        return True
    else:
        print(False)
        return False

string = input('Enter input ')
palindrome(string)
