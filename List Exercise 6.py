lista=[]
while True:
    num=input('Enter a number:')
    if num=='done':
        break
    else:
        try:
            num=float(num)
            lista.append(num)
        except:
            print('Please enter a number.')
            continue
maxi=max(lista)
mini=min(lista)
print('Maximum:',maxi)
print('Minimum:',mini)
