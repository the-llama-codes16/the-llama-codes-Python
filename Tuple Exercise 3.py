while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
import string
lettercount=dict()
for line in fhand:
    line=line.strip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.translate(line.maketrans('','',' '))
    line=line.translate(line.maketrans('','',string.digits))
    line=line.translate(line.maketrans('','','\t'))
    line=line.lower()
    for letter in line:
        lettercount[letter]=lettercount.get(letter,0)+1
letterfreq=list()
for letter,freq in lettercount.items():
    letterfreq.append((freq,letter))
letterfreq.sort(reverse=True)
for freq,letter in letterfreq:
    print(letter)
    
