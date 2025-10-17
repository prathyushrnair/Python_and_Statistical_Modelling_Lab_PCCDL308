"""
Write a program to **replace a word by another word in a sentence
"""
def replace(list_of_words,target,new_word):
    for index in range(len(list_of_words)):
        if list_of_words[index]==target:
            list_of_words[index]=new_word
    print(" ".join(list_of_words))
a=input('Enter a sentence')
b=input('Enter the word to be replaced')
c=input('Enter the new word')
replace(a.split(),b,c)
