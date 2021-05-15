fruit=input('Please enter name of a fruit:')
index=-1
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index-1
    if ((index*-1)==len(fruit)):
            print(fruit[0])
            break
print('Done!')
