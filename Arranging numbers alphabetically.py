word1=input('Enter word:')
word2=input('Enter another word:')
if word1<word2:
    print(word1,'comes before',word2+'.')
elif word1>word2:
    print(word1,'comes after',word2+'.')
elif word1==word2:
    print('They are the same words!')
