# -*- coding: utf-8 -*-
#
# You need to fill the blank line at the end of the source file.
#
from pydub import AudioSegment 
from gtts import gTTS
import os
import time

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

# Lang = vi, ja, en, km, zh-cn, ko, th
lang1 = "vi"
lang2 = "en"

print("Read the source file")

text_result  = ""
for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    sentence_id = splitLine[0]
    sentence_text = splitLine[1]
    print(sentence_id, sentence_text)    
    
    if  sentence_text.find("[") == -1:
        text_result = text_result + sentence_id + "\t" +  sentence_text + "\t" +"xxxx" + "\n" 
        sentence_text = ""
        continue 

    text1 = ""
    text2 = ""
    text_result =  text_result + sentence_id 
    while  sentence_text.find("[") > -1:
        start_text2 = sentence_text.find("[") + 1
        end_text2 = sentence_text.find("]")
        
        text1 = sentence_text[:start_text2-1]
        text2 = sentence_text[start_text2:end_text2]
        
        sentence_text = sentence_text.replace( text1 , "", 1)
        sentence_text = sentence_text.replace( "[" + text2 + "]" , "", 1)
        
        if text1 == "" : 
            text1 = "xxxx"
        if text2 == "" : 
            text2 = "xxxx"

        text_result = text_result  + "\t" +  text1 + "\t" + text2 
        
    if  len(sentence_text) > 0 :
        text_result = text_result + "\t" + sentence_text + "\t" +"xxxx" + "\n" 
    else:
        text_result = text_result + "\n"
        
result_file.write (text_result)
result_file.close()
source_file.close()

#create sound

source_file = open('result.txt', encoding='utf-8', mode='r')
silence = AudioSegment.silent(duration= 500)

print (".......................................")
print ("Create Sound")

for line in source_file :
    time.sleep(1)
    line = line.strip()
    li_word = line.split("\t")
    sentence_id  = li_word[0]
    li_word = li_word[1:]
    
    print(sentence_id, li_word)

    lang = lang1
    total_audio = AudioSegment.empty()
    for word in li_word :
        if lang == lang1:
            print(lang,"-", word)
            if word != "xxxx" : 
                tts = gTTS(word , lang = lang )
                tts.save("lang.mp3" )
                total_audio =  total_audio + AudioSegment.from_file("lang.mp3", format = "mp3")
            lang = lang2
        else: 
            print(lang,"-", word)
            if word != "xxxx" : 
                tts = gTTS(word , lang= lang)
                tts.save("lang.mp3" )
                total_audio =  total_audio + AudioSegment.from_file("lang.mp3", format = "mp3")
                lang = lang1

    total_audio.export(out_f = sentence_id + ".mp3",   format = "mp3")