lookup = {
  'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q',
  'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',
  'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y',
  'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
  'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
  'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
  'Y': 'L', 'Z': 'M'
}

def rot13(encodedStr):
  capitalized = encodedStr.upper()
  encodedList = list(capitalized)
  decodedList = []

  for letter in encodedList:
    if letter in lookup:
      letter = lookup[letter]
    decodedList.append(letter)

  decodedStr = ''.join(decodedList)
  print(decodedStr)
  return decodedStr

string = str(input('Enter input to decode using rot13 algorithm '))
rot13(string)
