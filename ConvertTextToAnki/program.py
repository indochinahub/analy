# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

OneLineText = ""
for line in source_file :
    line = line.strip()
#หากต้องการให้ตัดบรรทัด ตามการขั้นบรรทัดใหม่ ให้แก้เป็น line = line + "."
    line = line + " "
    OneLineText = OneLineText + line

OneLineText = OneLineText.replace(";","::")    
OneLineText = OneLineText.replace("U.S.","US ")    
OneLineText = OneLineText.replace("Mr.", "Mr")
OneLineText = OneLineText.replace("Mrs.", "Mrs")
OneLineText = OneLineText.replace("...", ".")
OneLineText = OneLineText.replace("\"", " ")


Sentences = OneLineText.split('.')

for sentence in Sentences :
    sentence = sentence.strip()
    result_file.write(sentence + '.\n' )     
