while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('Cannot open file:',fname)
        continue
daycount=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        seq=line.split()
        day=seq[2]
        daycount[day]=daycount.get(day,0)+1
    else:
        continue
print(daycount)
