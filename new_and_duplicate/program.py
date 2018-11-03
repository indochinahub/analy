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

#check for dublicate in root_word_list[]
root_word_list = []
i = 1
for line in word_list_file :
    line = line.strip(' \t\n\r,')
    line = line.lower()
    line = line.split(",")
    
    # line[0] contains a root words.
    if line[0] in root_word_list :
        print ( "Worldlist dupilate at : " +  str(i) )
    else :
        root_word_list.append(line[0])
        
    
    #put all words in word_dict[]
    j = 0
    for word in line :
        word_key = str(len(word)).zfill(2) + str(i).zfill(4) + str(j).zfill(2)
        #int(str(len(word)) + str(i) + str(j)) ;
        word_dict[word] = word_key;
        j = j+1 
        
    i = i + 1    

print (root_word_list)    
word_tuple = ()
word_tuple = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True   )


word_dict = {} 
for w in word_tuple :
    word_dict[w[0]] = w[1]
    

vocab_in_file = []
for line in target_file :
    vocab_in_sentence = []
    origin_line = line
    line = line.lower()
    #word_dict_for_replace = copy.deepcopy(word_dict)
    for word in word_dict:
        if word in line :
            if  word  not in vocab_in_file :
                vocab_in_file.append(word)
                vocab_in_sentence.append(word)
                
            line = line.replace(word, "xx ")


    for v in vocab_in_sentence :
        if word_dict[v][-2:] != '00' :
            for w in word_dict :
                if (word_dict[w][2:6] == word_dict[v][2:6]) and (word_dict[w][-2:] == '00') :
                    result_file.write( v + "->" + w +'\n' )
        else :
            result_file.write( v + '\n' )
        
    result_file.write( line )
#    result_file.write( origin_line)


result_file.close()