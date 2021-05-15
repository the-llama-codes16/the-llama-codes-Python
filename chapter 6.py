strr='X-DSPAM-Confidence:0.8475'
colpos=strr.find(':')
num=strr[colpos+1:]
num=float(num)
print(num)
