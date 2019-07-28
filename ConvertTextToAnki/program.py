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
OneLineText = OneLineText.replace("-", ":")
OneLineText = OneLineText.replace("...", ".")
OneLineText = OneLineText.replace("\"", " ")
OneLineText = OneLineText.replace("1.", "1 ")
OneLineText = OneLineText.replace("2.", "2 ")
OneLineText = OneLineText.replace("3.", "3 ")
OneLineText = OneLineText.replace("4.", "4 ")
OneLineText = OneLineText.replace("5.", "5 ")
OneLineText = OneLineText.replace("6.", "6 ")
OneLineText = OneLineText.replace("7.", "7 ")
OneLineText = OneLineText.replace("8.", "8 ")
OneLineText = OneLineText.replace("9.", "9 ")
OneLineText = OneLineText.replace("r.", "r ")
OneLineText = OneLineText.replace("i.e.", "i e ")
OneLineText = OneLineText.replace(". . . .", "---")
OneLineText = OneLineText.replace(". . .", "---")
OneLineText = OneLineText.replace("J.D.M.", "J-D-M ")
OneLineText = OneLineText.replace("Mt.", "Mt  ")
OneLineText = OneLineText.replace("e.g.", "e-g ")
OneLineText = OneLineText.replace("Y.", "Y ")
OneLineText = OneLineText.replace("A.", "A ")
OneLineText = OneLineText.replace("Thommanon.", "Thommanon ")
OneLineText = OneLineText.replace("A.", "A ")
OneLineText = OneLineText.replace("B.", "B ")
OneLineText = OneLineText.replace("C.", "C ")
OneLineText = OneLineText.replace("D.", "D ")
OneLineText = OneLineText.replace("E.", "E ")
OneLineText = OneLineText.replace("F.", "F ")
OneLineText = OneLineText.replace("G.", "G ")
OneLineText = OneLineText.replace("H.", "H ")
OneLineText = OneLineText.replace("I.", "I ")
OneLineText = OneLineText.replace("J.", "J ")
OneLineText = OneLineText.replace("K.", "K ")
OneLineText = OneLineText.replace("H.", "H ")
OneLineText = OneLineText.replace("I.", "I ")
OneLineText = OneLineText.replace("J.", "J ")
OneLineText = OneLineText.replace("K.", "K ")
OneLineText = OneLineText.replace("I.", "I ")
OneLineText = OneLineText.replace("J.", "J ")
OneLineText = OneLineText.replace("K.", "K ")
OneLineText = OneLineText.replace("L.", "L ")
OneLineText = OneLineText.replace("M.", "M ")
OneLineText = OneLineText.replace("N.", "N ")
OneLineText = OneLineText.replace("O.", "O ")
OneLineText = OneLineText.replace("P.", "P ")
OneLineText = OneLineText.replace("Q.", "Q ")
OneLineText = OneLineText.replace("R.", "R ")
OneLineText = OneLineText.replace("S.", "S ")
OneLineText = OneLineText.replace("T.", "T ")
OneLineText = OneLineText.replace("U.", "U ")
OneLineText = OneLineText.replace("V.", "V ")
OneLineText = OneLineText.replace("W.", "W ")
OneLineText = OneLineText.replace("X.", "X ")
OneLineText = OneLineText.replace("Y.", "Y ")
OneLineText = OneLineText.replace("Z.", "Z ")


OneLineText = OneLineText.replace("Lt.", "Lt ")
OneLineText = OneLineText.replace("Col.", "Col ")
OneLineText = OneLineText.replace("Z.", "Z ")





Sentences = OneLineText.split('.')

for sentence in Sentences :
    sentence = sentence.strip()
    result_file.write(sentence + '.\n' )     
