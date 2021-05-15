while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File does not exist:',fname)
        continue
import random
lista=[]
salitadict=dict()
for line in fhand:
    line=line.rstrip()
    wordlista=line.split()
    for word in wordlista:
        if word in lista:
            continue
        else:
            lista.append(word)
            salitadict[word]=random.random()
