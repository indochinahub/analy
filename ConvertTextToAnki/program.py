# -*- coding: utf-8 -*-

import re

# Function
def  separate(list_sentence, seperator ):
    list_dummy = []
    for sentence in list_sentence:
        list_sub_sentence = sentence.split(seperator)
        if len(list_sub_sentence) > 1: 
            for sub_sentence in list_sub_sentence: 
                sub_sentence = sub_sentence.strip()
                # When the last string are "?"or";" ect, we will get "" element after spliting
                # so we need to skip it.
                if sub_sentence != "" and sub_sentence[-1] != ".":
                    list_dummy.append(sub_sentence.strip() + seperator )
                else:
                    list_dummy.append(sub_sentence.strip() )
        else:
            list_dummy.append(sentence)
    return list_dummy


# main program
source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

txt_oneline = ""
for line in source_file :
    line = line.strip()
    line = line + " "
    txt_oneline = txt_oneline + line
txt_oneline = txt_oneline.strip()    

list_sentence = txt_oneline.split(".")

list_dummy = []
for sentence in list_sentence:
    sentence = sentence.strip() + "."

    #Edit here
    sentence = sentence.replace("?.", "?")
    sentence = sentence.replace(";.", ";")

    list_dummy.append(sentence)
list_sentence =  list_dummy
print(list_sentence)


list_sentence = separate(list_sentence, "?" )
#list_sentence = separate(list_sentence, ";" )
#print(list_sentence)

txt_oneline = ""
for sentence in list_sentence:
    txt_oneline = txt_oneline + sentence + "\n"

result_file.write(txt_oneline)


'''
OneLineText = OneLineText.replace(";","::")    
OneLineText = OneLineText.replace("U.S.","US ")    
OneLineText = OneLineText.replace("Mr.", "Mr")
OneLineText = OneLineText.replace("Mrs.", "Mrs")
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
OneLineText = OneLineText.replace("Inc.", "Inc ")
OneLineText = OneLineText.replace("St.", "St ")
'''