lookup = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
    90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}

def convertToRoman(num):
    romanized = ''
    for i in lookup:
        while i <= num:
            romanized += lookup[i]
            num -= i
    print(romanized)
    return romanized

number = int(input('Enter number to be converted to Roman numeral '))
convertToRoman(number)
