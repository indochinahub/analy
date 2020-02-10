# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re
import pinyin

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

OneLineText = ""
for line in source_file :
    line = line.strip()
    line = pinyin.get(line, format="diacritical", delimiter=" ")
    
    result_file.write(line + '\n' )     


