while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened:',fname)
        continue
sendict=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        wordlista=line.split()
        for word in wordlista:
            sender=wordlista[1]
            sendict[sender]=sendict.get(sender,0)+1
    else:
        continue
print(sendict)
maxkey=None
maxval=None
for sender in sendict:
    if maxval is None or sendict[sender]>maxval:
        maxkey=sender
    else:
        continue
print(maxkey,sendict[maxkey])
