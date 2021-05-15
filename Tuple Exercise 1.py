while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('Please enter a valid file.')
        continue
senders=dict()
for line in fhand:
    if line.startswith('From '):
        line=line.rstrip()
        wordlista=line.split()
        usender=wordlista[1]
        senders[usender]=senders.get(usender,0)+1
    else:
        continue
senderlista=list()
for sender,freq in senders.items():
    senderlista.append((freq,sender))
senderlista.sort(reverse=True)
nsenderlista=list()
for freq,sender in senderlista:
    nsenderlista.append((sender,freq))
print(nsenderlista[0])

    
