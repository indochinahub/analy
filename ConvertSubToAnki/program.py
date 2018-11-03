# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

i = 0
sentence = ""
for line in source_file :
    line = line.strip(' \t\n\r,')
    line.replace(";", "::")
    line.replace("<i>", "")
    line.replace("</i>", "")
    if line.isdigit() :
        i = 0
        sentence_number = line
        sentence = "" 
    else : 
        i = i + 1

    if i > 1 :
        sentence =  sentence + " " + line
    
    if line == "" :
        result_file.write( sentence + '\n')    
#        result_file.write(sentence_number + "\t" + sentence + '\n')    

        
    
    
    
    
    
        
        
    
    
result_file.write( line )    
    
    
    
    