word=input('Enter a word:')
d=dict()
for letter in word:
    d[letter]=d.get(letter,0)+1
print(d)
