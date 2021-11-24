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
    #text_to_write = text_to_write + arr_text[1] + "\t"
    text_to_write = text_to_write + arr_text[2] + "\t"
    text_to_write = text_to_write + arr_text[3] + "\t"
    
    #question
    raw_question = arr_text[4]
    
    #choice
    if arr_text[5] == "NULL" :
        choice = raw_question[raw_question.find("(")+1 :raw_question.find(")")]
        text_to_write = text_to_write + "[ " + choice + " ]" + "\t"
    else :
        choice = arr_text[5];
        text_to_write = text_to_write + "[ " + choice + " ]" + "\t"
    
    
    
    answer_in_bracket = raw_question[raw_question.find("{{")+2 :raw_question.find("}}")]
    answer = answer_in_bracket.replace("c1::","")
    text_to_write = text_to_write + answer + "\t"
    
    question_with_dot = raw_question.replace("{{"+answer_in_bracket+"}}", "...")
    question_with_dot = question_with_dot.replace("("+choice+")", "")
    question_with_dot = question_with_dot.replace("{{c1::", "")
    question_with_dot = question_with_dot.replace("}}", "")    
    
    
    text_to_write = text_to_write + question_with_dot + "\t"
    
    question_to_sound = raw_question.replace("{{"+answer_in_bracket+"}}", answer)
    question_to_sound = question_to_sound.replace("("+choice+")", "")
    question_to_sound = question_to_sound.replace("{{c1::", "")
    question_to_sound = question_to_sound.replace("}}", "")
    
    question_to_sound = question_to_sound.replace("<br>",  " " )
    text_to_write = text_to_write + question_to_sound
    
    
    text_to_write = text_to_write + "\n"
    print(arr_text[0])

result_file.write( text_to_write )    

