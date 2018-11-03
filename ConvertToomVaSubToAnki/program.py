# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
import random

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

def RandText( mytext) :
    randText = ""
    RANDOM_VALUE = 20
    for charactor in mytext :
        # เช็คว่าเป็นตัวอักษรหรือไม่
        if charactor.isalpha() :
            if  random.randint(0,100) >= RANDOM_VALUE :
                print ("found")
                randText = randText  +  charactor
            else :
                print ("not found")        
                randText = randText  + "_ "
                
        # กรณีเป็นสัญลักษณ์อื่นๆ 
        else :
            randText = randText  +  charactor
                
    return randText ;


i = 0
sentence = ""
for line in source_file :
    line = line.strip(' \t\n\r,')
    if  line[0:2].isdigit() :
        i = 0

    i = i + 1
    if  i == 1 :
        print (" is digit : " + line) 
        text = ""
    elif i == 3 :
        print ("English:" + line) 
        text = line
    elif i == 5 :
        print ("  Vietnamese :  " + line)        
        text = text + "::"  +   RandText( line) + " ; " + line
        result_file.write( "Tiếng Anh Lớp 3(Tập 2) :: " + text + "\n")
    

    
    
    
    