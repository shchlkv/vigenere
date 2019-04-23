'''
seaching letter of WORD in ALPHABET
get index of letter from ALPHABET

'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
alphabet=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
#keyword=list('бетономешалкавйъчыгыхеаюукй')               #password or keyword
#word=list('безинформатикинетникчемноесуществованиеэтогомирабудущегоиникодганебудетмирбезмашинэтонемирэтопостноесуществованиекогдаянапочтеслужилямщикоомА')

indexes_of_keyword=[]           # list, which will to contain indices of keyword
indexes_of_word=[]              # list, which will to contain indices of word
crypt_word=[]
indexes_of_cript_word=[]
decrypt_word=[]

word=input('Enter any word or phrase wich need to encrypt. The phrase should be without spaces and with only cyrillic letters: ')
keyword=input('Enter keyword to encrypt the phrase: ')




for i in range(len(keyword)):
        if keyword[i] in alphabet:          #cheking of letters from list 'keyword' with index 'i' in list 'alphabet'
                letter=keyword[i]           #this variable 'letter' contains letter from list 'keyword' with index 'i'. 
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                indexes_of_keyword.append(index_of_letter_from_list_alphabet)  # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 
               
for i in range(len(word)):
        if word[i] in alphabet:         #cheking of letters from list 'word' with index 'i' in list 'alphabet'
                letter=word[i]          #this variable 'letter' contains letter from list 'word' with index 'i'.
                index_of_letter_from_list_alphabet=alphabet.index(letter) #this variable contains index of letter from 'alphabet' list
                indexes_of_word.append(index_of_letter_from_list_alphabet)        # insert 'index_of_letter_from_list_alphabet' in  list 'indexes_of_keyword' 


# calculation of cryptword
n=len(word)
i=0
j=0
while n > 0:
        new_index_letter=(indexes_of_keyword[i]+indexes_of_word[j])%33
        new_cript_letter=alphabet[new_index_letter]
        crypt_word.append(new_cript_letter)
        n-=1
        i+=1
        j+=1
        if i==len(keyword):
                i=0

print(''.join(word))
print(''.join(keyword))
print(''.join(crypt_word))


for i in range(len(word)):
        if crypt_word[i] in alphabet:         
                letter=crypt_word[i]          
                index_of_letter_from_list_alphabet=alphabet.index(letter) 
                indexes_of_cript_word.append(index_of_letter_from_list_alphabet)  

n=len(word)

i=0
j=0
while n > 0:
        new_index_letter_decrypt=(indexes_of_cript_word[j]-indexes_of_keyword[i]+33)%33
        new_decript_letter=alphabet[new_index_letter_decrypt]
        decrypt_word.append(new_decript_letter)
        n-=1
        i+=1
        j+=1
        if i==len(keyword):
                i=0

print(''.join(decrypt_word))


'''-fragmet of code, which write crypting text in file-'''
                
