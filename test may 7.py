lista=list()
fhand=open('romeo.txt')
for line in fhand:
    line=line.rstrip()
    wordlista=line.split()
    for word in wordlista:
        if word in lista:
            continue
        else:
            lista=lista.append(word)
            
