while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened:',fname)
        continue
counts=dict()
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
keylist=list(counts.keys())
keylist.sort()
print(keylist)
for key in keylist:
    print(key+':',counts[key])
    
