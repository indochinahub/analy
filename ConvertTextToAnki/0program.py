# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

def ZeroFill ( myNumber ) :
    digitNumber = 3
    ZeroFilledNumber =   ((digitNumber - len(myNumber))* "0" ) + myNumber
    return ZeroFilledNumber


j = 0
OneLineText = ""
for line in source_file :
    line = line.strip()
#หากต้องการให้ตัดบรรทัด ตามการขั้นบรรทัดใหม่ ให้แก้เป็น line = line + ". "
    line = line + " "
    OneLineText = OneLineText + line

# Adapt according to the source.
OneLineText.replace(";", "::")
OneLineText.replace("Mr.", "Mr")
OneLineText.replace("Mrs.", "Mrs")
OneLineText.replace("...", ".")
OneLineText.replace("“", "\"")
OneLineText.replace("”", "\"")
OneLineText.replace("\"\"", "\"")
OneLineText.replace("\"\"\"", "\"")

#สัญลักษณ์สำหรับการตัดบรรทัด 
Sentences = OneLineText
#Sentences = OneLineText.split('.')

for Sentence in Sentences :
    #Sentence = Sentence.lstrip("\"")
    #Sentence = Sentence.lstrip("\“")
    Sentence = Sentence.strip()
#    result_file.write (  Sentence + '.' + '\n')   เติม . ต่อท้าย, แต่ในภาษาเวียดนาม พบว่าไม่ควรเติม . ท้ายประโยค เพราะจะอ่านเครื่องหมายนี้ด้วย
#ภาษาเวียดนาม ควรใช้แบบนี้ (ไม่มี . ท้ายประโยค) เพราะ google จะอ่าน " . " ด้วย  result_file.write (  Sentence +  '\n') 
    result_file.write (  Sentence + '.' + '\n') 
