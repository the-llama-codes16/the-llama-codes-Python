while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
domainlist=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        wordlista=line.split()
        sender=wordlista[1]
        atpos=sender.find('@')
        domain=sender[atpos+1:]
        domainlist[domain]=domainlist.get(domain,0)+1
    else:
        continue
print(domainlist)
