fname=input('Enter file name:')
fhand=open(fname)
lista=[]
for line in fhand:
    line=line.rstrip()
    wordlista=line.split()
    for word in wordlista:
        if word in lista:
            continue
        else:
            lista.append(word)
lista.sort()
print(lista)
        
        
