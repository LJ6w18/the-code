a = input("Please Enter a Sentence: ")
a = a.lower()

letters = {}
for char in a:
    if char.isalpha():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

for entry in letters:
   print('{:s} : {:d}'.format(entry,letters[entry])) 