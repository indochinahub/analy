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
    line_texts = line.split("\t")
    word = line_texts[0]
    
    #result_file.write( word + '\n' )
    #line_texts[1] = line_texts[1].replace("(1)"," ")
    #line_texts[1] = line_texts[1].replace("(2)"," ")
    #line_texts[1] = line_texts[1].replace("(3)"," ")
    #line_texts[1] = line_texts[1].replace("(4)"," ")
    #line_texts[1] = line_texts[1].replace("(5)"," ")
    #line_texts[1] = line_texts[1].replace("(6)"," ")
    #line_texts[1] = line_texts[1].replace("(7)"," ")
    #line_texts[1] = line_texts[1].replace("(8)"," ")
    #line_texts[1] = line_texts[1].replace("(9)"," ")
    #line_texts[1] = line_texts[1].replace("(10)"," ")
    #line_texts[1] = line_texts[1].replace("(11)"," ")
    #line_texts[1] = line_texts[1].replace("(12)"," ")
    #line_texts[1] = line_texts[1].replace("(13)"," ")
    #line_texts[1] = line_texts[1].replace("(14)"," ")
    
    line_texts[1] = line_texts[1].replace(";","::")    
    line_texts[1] = line_texts[1].replace("U.S.","US ")    
    line_texts[1] = line_texts[1].replace("Mr.", "Mr")
    line_texts[1] = line_texts[1].replace("Mrs.", "Mrs")
    line_texts[1] = line_texts[1].replace("-", ":")
    line_texts[1] = line_texts[1].replace("...", ".")
    line_texts[1] = line_texts[1].replace("\"", " ")
    line_texts[1] = line_texts[1].replace("1.", "1 ")
    line_texts[1] = line_texts[1].replace("2.", "2 ")
    line_texts[1] = line_texts[1].replace("3.", "3 ")
    line_texts[1] = line_texts[1].replace("4.", "4 ")
    line_texts[1] = line_texts[1].replace("5.", "5 ")
    line_texts[1] = line_texts[1].replace("6.", "6 ")
    line_texts[1] = line_texts[1].replace("7.", "7 ")
    line_texts[1] = line_texts[1].replace("8.", "8 ")
    line_texts[1] = line_texts[1].replace("9.", "9 ")
    line_texts[1] = line_texts[1].replace("r.", "r ")
    line_texts[1] = line_texts[1].replace("i.e.", "i e ")
    line_texts[1] = line_texts[1].replace(". . . .", "---")
    line_texts[1] = line_texts[1].replace(". . .", "---")
    line_texts[1] = line_texts[1].replace("J.D.M.", "J-D-M ")
    line_texts[1] = line_texts[1].replace("Mt.", "Mt  ")
    line_texts[1] = line_texts[1].replace("e.g.", "e-g ")
    line_texts[1] = line_texts[1].replace("Y.", "Y ")
    line_texts[1] = line_texts[1].replace("A.", "A ")
    line_texts[1] = line_texts[1].replace("Thommanon.", "Thommanon ")
    line_texts[1] = line_texts[1].replace("A.", "A ")
    line_texts[1] = line_texts[1].replace("B.", "B ")
    line_texts[1] = line_texts[1].replace("C.", "C ")
    line_texts[1] = line_texts[1].replace("D.", "D ")
    line_texts[1] = line_texts[1].replace("E.", "E ")
    line_texts[1] = line_texts[1].replace("F.", "F ")
    line_texts[1] = line_texts[1].replace("G.", "G ")
    line_texts[1] = line_texts[1].replace("H.", "H ")
    line_texts[1] = line_texts[1].replace("I.", "I ")
    line_texts[1] = line_texts[1].replace("J.", "J ")
    line_texts[1] = line_texts[1].replace("K.", "K ")
    line_texts[1] = line_texts[1].replace("H.", "H ")
    line_texts[1] = line_texts[1].replace("I.", "I ")
    line_texts[1] = line_texts[1].replace("J.", "J ")
    line_texts[1] = line_texts[1].replace("K.", "K ")
    line_texts[1] = line_texts[1].replace("I.", "I ")
    line_texts[1] = line_texts[1].replace("J.", "J ")
    line_texts[1] = line_texts[1].replace("K.", "K ")
    line_texts[1] = line_texts[1].replace("L.", "L ")
    line_texts[1] = line_texts[1].replace("M.", "M ")
    line_texts[1] = line_texts[1].replace("N.", "N ")
    line_texts[1] = line_texts[1].replace("O.", "O ")
    line_texts[1] = line_texts[1].replace("P.", "P ")
    line_texts[1] = line_texts[1].replace("Q.", "Q ")
    line_texts[1] = line_texts[1].replace("R.", "R ")
    line_texts[1] = line_texts[1].replace("S.", "S ")
    line_texts[1] = line_texts[1].replace("T.", "T ")
    line_texts[1] = line_texts[1].replace("U.", "U ")
    line_texts[1] = line_texts[1].replace("V.", "V ")
    line_texts[1] = line_texts[1].replace("W.", "W ")
    line_texts[1] = line_texts[1].replace("X.", "X ")
    line_texts[1] = line_texts[1].replace("Y.", "Y ")
    line_texts[1] = line_texts[1].replace("Z.", "Z ")
    line_texts[1] = line_texts[1].replace("Lt.", "Lt ")
    line_texts[1] = line_texts[1].replace("Col.", "Col ")
    line_texts[1] = line_texts[1].replace("Inc.", "Inc ")
    line_texts[1] = line_texts[1].replace("St.", "St ")
    line_texts[1] = line_texts[1].replace("etc.", "etc ")

    
    EnExampleSentences = line_texts[1].split(".")
    print(line_texts[1] + "xxx" + line_texts[2] + "\n")
    
    
    for sentence in EnExampleSentences:
        
        
        sentence = sentence.strip()
        if len(sentence) :
            result_file.write( sentence +".\t" + word + '\n' )

