# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

OneLineText = ""
Sentences = []
for line in source_file :
    
    line = re.sub(r"\[.*?\]", "", line)
    line = line.strip()
    
    result_file.write(line + '.\n' )
    
    #startBracket = line.find("[")
    #if( startBracket >= 0 ) :
    #    endBracket = line.find("]")
    #    bracketText = line[startBracket:(endBracket-startBracket) + 1]
    #    print(bracketText)
        
    





def my_function():
  print("Hello from a function")
