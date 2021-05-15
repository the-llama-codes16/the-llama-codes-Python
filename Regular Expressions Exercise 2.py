import re
fname=input('Enter file:')
fhand=open(fname)
count=0
total=0
for line in fhand:
    line=line.rstrip()
    lst=re.findall('^New Revision: ([0-9]+)',line)
    if len(lst)>0:
        for mem in lst:
            num=float(mem)
            count=count+1
            total=total+num
ave=total/count
print(ave)
        
