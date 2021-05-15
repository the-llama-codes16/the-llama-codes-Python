fname=input('Enter file name:')
fhand=open(fname)
count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        count=count+1
        wordlista=line.split()
        print(wordlista[1])
    else:
        continue
print('There were',count,'lines in the file with From as the first word.')
