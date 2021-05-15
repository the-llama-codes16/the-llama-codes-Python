while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
hourdict=dict()
for line in fhand:
    if line.startswith('From '):
        line=line.rstrip()
        wordlista=line.split()
        hour=wordlista[5]
        colpos=hour.find(':')
        time=hour[:colpos]
        hourdict[time]=hourdict.get(time,0)+1
    else:
        continue
hflista=list()
for hour,freq in hourdict.items():
    hflista.append((hour,freq))
hflista.sort()
for hour,freq in hflista:
    print(hour,freq)
    
