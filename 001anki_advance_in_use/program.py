# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#

import re

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

text_to_write = "";
for line in source_file :
    line = line.strip()
    arr_text = line.split("\t")
    
    text_to_write = text_to_write + "'" + arr_text[0] + "\t"
    text_to_write = text_to_write + arr_text[1] + "\t"
    text_to_write = text_to_write + arr_text[2] + "\t"
    
    sentence = arr_text[3]
    word_in_bracket = sentence[sentence.find("{{")+2 :sentence.find("}}")]
    #text_to_write = text_to_write + word_in_bracket + "\t"
    
    
    if sentence.find("<u>") != -1  and sentence.find("</u>") != -1 :
        choice = sentence[sentence.find("<u>")+3 : sentence.find("</u>")]
        choice_in_tag =  "<u>" + choice + "</u>"
        choice = "[ " + choice + " ]"
        
        
    else :
        choice = arr_text[4].strip()
        choice = choice.replace( ";", " ; ")
        choice_in_tag =  "xxxxxxxxxxxxxxxxxx"
        choice = "[ " + choice +" ]"
        
        
    text_to_write = text_to_write + choice  + "\t"
    
    answer = word_in_bracket.replace("c1::","")
    text_to_write = text_to_write + answer + "\t"
    

    sentence = sentence.replace( choice_in_tag , "")
    #text_to_write = text_to_write + sentence + "\t"
    
    answer_in_bracket = sentence[sentence.find("{{") :sentence.find("}}")+2]
    #text_to_write = text_to_write + answer_in_bracket + "\t"    
    
    sentence_with_blank = sentence.replace(answer_in_bracket, "...")
    text_to_write = text_to_write + sentence_with_blank + "\t"
    
    sentence_full = sentence.replace(answer_in_bracket, answer)
    text_to_write = text_to_write + sentence_full


   

    
    choice_text = arr_text[4].strip()
    choice_text = choice_text.replace( ";", " ; ")
    choice_text = "[ " + choice_text +" ]"
    #text_to_write = text_to_write + choice_text + "\t"
    
    
    
    
    
    
    


    
    
    text_to_write = text_to_write + "\n"
    print(arr_text[0])
    
    
    
    
result_file.write( text_to_write )    

