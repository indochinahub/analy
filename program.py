# -*- coding: utf-8 -*-

import string
import sys
import operator


# อ่านพจนานุกรมมาเก็บไว้ใน ลิสท์ word_list ก่อน
#word_list_file = open('wordlist.txt', 'r')
#target_file = open('source.txt', 'r')
#result_file = open('result.txt', 'w')


word_list_file = open('wordlist.txt', encoding='utf-8', mode='r')
target_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')


word_dict = {} 
i = 1
#check for dublicate
word_list = []
i = 1
for line in word_list_file :
    line = line.strip(' \t\n\r')
    line = line.lower()
    if line in word_list :
        print ( "Worldlist dupilate at : " +  str(i) )
    else :
        word_list.append(line)
        
    word_dict[line] = len(line) ;
    i = i + 1    
    
#word_dict = sorted(word_dict.items(), key=operator.itemgetter(1))

print (word_dict)
word_tuple = ()
word_tuple = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True   )
print (word_tuple)

word_dict = {} 
for w in word_tuple :
    word_dict[w[0]] = w[1]


for line in target_file :
    vocab_in_sentence = []
    origin_line = line
    line = line.lower()
    for word in word_dict:
        if word in line :
            if  word_dict[word] != 0 :
                vocab_in_sentence.append(word)
            line = line.replace(word, "xx ")
            word_dict[word] = 0 

    for v in vocab_in_sentence :
            result_file.write( v + '\n' )
        
    result_file.write( line )
#    result_file.write( origin_line)


result_file.close()