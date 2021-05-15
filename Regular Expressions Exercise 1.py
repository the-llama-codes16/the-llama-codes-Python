import re
regexp=input('Enter a regular expression:')
fhand=open('mbox.txt')
count=0
for line in fhand:
    line=line.rstrip()
    if re.search(regexp,line):
        count=count+1
print('mbox.txt had',count,'lines that matched',regexp)
        
