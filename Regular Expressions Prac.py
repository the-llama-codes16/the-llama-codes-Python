#Using Regular Expressions library to look for lines containing 'From:'
#while using the search function
fname=input('Enter file name:')
fhand=open(fname)
import re
for line in fhand:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)
fname=input('Enter file name:')

#Using Regular Expressions library to look for lines starting with 'From:'
#while using the search function and ^
fhand=open(fname)
import re
for line in fhand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)

#Using Regular Expressions library to look for lines starting with 'F'
#and ending with 'm:' with 2 characters in between
#while using the search function and ^
fname=input('Enter file name:')
fhand=open(fname)
import re
for line in fhand:
    line=line.rstrip()
    if re.search('^F..m:',line):
        print(line)


import re
s='A message from csev@umich.edu to cwen@iupui.edu about meeting @2pm.'
lst=re.findall('\S+@\S+',s)
print(lst)


import re
while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('Please enter valid file name.')
        continue
for line in fhand:
    line=line.rstrip()
    lst=re.findall('\S+@\S+',line)
    if len(lst)>0:
        print(lst)



import re
while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
for line in fhand:
    line=line.rstrip()
    lst=re.findall('[0-9a-zA-Z]\S*@\S*[0-9a-zA-Z]',line)
    if len(lst)>0:
        print(lst)



while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
import re
for line in fhand:
    line=line.rstrip()
    lst=re.findall('X-.*: [0-9.]+',line)
    if len(lst)>0:
        print(lst)




while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
import re
for line in fhand:
    line=line.rstrip()
    lst=re.findall('^Details:.*rev=([0-9]+)',line)
    if len(lst)>0:
        print(lst)


while True:
    fname=input('Enter file name:')
    try:
        fhand=open(fname)
        break
    except:
        print('File cannot be opened.')
        continue
import re
for line in fhand:
    line=line.rstrip()
    lst=re.findall('^From .* ([0-9][0-9]):',line)
    if len(lst)>0:
        print(lst)



import re
x='We just received $10 for cookies.'
y=re.findall('\$[0-9.]+',x)
print(y)












