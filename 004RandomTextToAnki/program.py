# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import random
source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

def RandText(mytext) :

    interval = 5
    randText = ""
    #RANDOM_VALUE = 50

    if len(mytext) <= 1:
        return "*"
    
    if len(mytext) <= 2:
        my_list = list(mytext)
        my_list[1] = "*"
        return "".join(my_list)
   
    if len(mytext) <= interval:
        my_list = list(mytext)
        my_list[  int(len(mytext) / 2)   ] = "*"
        return "".join(my_list)

    
    i = 1
    for charactor in mytext :
        # เช็คว่าเป็นตัวอักษรหรือไม่
        if charactor.isalpha() :
            if i == interval :
                print ("the new char")        
                randText = randText  + "*"
                i = 1		
            elif  i != interval :
                print ("the same char")
                randText = randText  +  charactor
                i = i + 1

        # กรณีเป็นสัญลักษณ์อื่นๆ 
        else :
            randText = randText  +  charactor
          
    return randText ;

j = 0
sentence = ""
for line in source_file :
#ตัดอักษรขึ้นบรรทัดใหม่ออกไปเลย
    line = line.strip()
    line = line.replace(";", "::")
    line = line.replace("Mr.", "Mr")
    line = line.replace("Mrs.", "Mrs")
    line = line.replace("Mrs.", "Mrs")
    
    if not line == '' :
        sentences = []
        #sentences = line.split('។')
        sentences = line.split('\n')
        for i in sentences :
            i = i.strip()
 
            if len(i) <= 0 :
                pass
            else :
                j = j + 1
                
                result_file.write ("["+ RandText( i ) +"]\n")
                
#        for sentence in sentences :
#            result_file.write( "xxx" + '\n')    
 
result_file.close()


# test

#result_file.write ( "Wizard-of-Oz-c24-"+ str(j) + "  " + i + ". ; " + RandText ( i ) +"\n ")
#result_file.write ( "Got-b01-c015-"+ str(j) + "  " + i +'. ; "Catelyn" \n')
#result_file.write ( "04-រដ្ឋធម្មនុញ្ "+ str(j) + "  " + i + ". ; " + RandText ( i ) +"\n")
