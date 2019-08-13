# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

sentences = []
i = 1
en = ""
th = ""

for line in source_file :
    

    
    line = re.sub(r"\[.*?\]", "", line)
    line = line.strip()
    
    if line.find("\t") < 0 :
        print("no tab at ::" + i)
    else :
        line = line.split("\t")
    
    if ( line[0][-1] != ".") :
        en = en + line[0]
        th = th + line[1]
    else : 
        en = en + line[0]
        th = th + line[1]
        result_file.write(en + "\t" + th + "\n" )
        en = ""
        th = ""
    

    
    
    i = i + 1


#for line in source_file :
#    line = re.sub(r"\[.*?\]", "", line)
#    line = line.strip()   
#    result_file.write(line + '.\n' )
    

        
    





def my_function():
  print("Hello from a function")
