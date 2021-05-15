fname=input('Enter file name:')
try:
    fhand=open(fname)
except:
    print('File does not exist.')
    exit()
count=0
total=0
talla=len('X-DSPAM-Confidence: ')
for line in fhand:
    if line.startswith('X-SPAM-Confidence: '):
        count=count+1
        extr=line[talla:]
        extr=float(extr)
        total=total+extr
    else:
        continue
if count!=0:
    ave=total/count
    print('Average spam confidence:',ave)
else:
    print('Nothing')
   
        
        
        
        
    
