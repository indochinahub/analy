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

b_sound = False

#Delete *.mp3
for folder, subfolder, files in os.walk('.') : 
    for file in files : 
        if file.endswith('.mp3') :
            path = os.path.join(folder, file)
            os.remove(path)
            print("Delete : " ,path)
        
sum_mp3a = AudioSegment.empty()
sum_mp3b = AudioSegment.empty()
sum_mp3ab = AudioSegment.empty()
silence = AudioSegment.silent(duration= 500)

sum_text_a  = ""
sum_text_b  = ""
#paragraph_seperator = "\n.\n"
paragraph_seperator = "\t\n"

for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    
    text_id = splitLine[0]
    
    # Lang = vi, ja, en, km, zh-cn, ko, th
    
    # For a
    language_a = splitLine[1]
    text_a = splitLine[2].strip()
    filename_a = text_id.strip() +"a.mp3" 

    if text_a == 'xxxx' :
        silence.export(out_f = filename_a,   format = "mp3")
    else : 
        tts = gTTS(text_a , lang= language_a )
        tts.save( filename_a )

    mp3a = AudioSegment.from_file(file = filename_a, format = "mp3") 
    sum_mp3a = sum_mp3a + silence + mp3a
    sum_text_a  = sum_text_a + paragraph_seperator + text_a

    # For b    
    if b_sound ==  True :
        language_b = splitLine[3]
        text_b = splitLine[4].strip()
        filename_b = text_id.strip() +"b.mp3" 

        if text_b == 'xxxx' :
            silence.export(out_f = filename_b,   format = "mp3")
        else : 
            tts = gTTS(text_b , lang= language_b )
            tts.save( filename_b )

        mp3b = AudioSegment.from_file(file = filename_b, format = "mp3") 
        sum_mp3b = sum_mp3b + silence + mp3b
        sum_text_b  = sum_text_b + paragraph_seperator + text_b
        # For ab
        sum_mp3ab = sum_mp3ab + silence  + mp3a + silence  + mp3b
        print( filename_a + "\t" + text_a + "\n" + filename_b + "\t" + text_b )
        
    else:
        print( filename_a + "\t" + text_a)
    
    time.sleep(2)
    
result_file.write (sum_text_a + sum_text_b)
result_file.close()

sum_mp3a.export(out_f = "sum_mp3a.mp3",   format = "mp3")
#sum_mp3a.export(out_f = "E:\\lesson_media\\TH011\\mp3\\sum_mp3a.mp3",   format = "mp3")



if b_sound ==  True :
    sum_mp3b.export(out_f = "sum_mp3b.mp3",   format = "mp3")
    sum_mp3ab.export(out_f = "sum_mp3ab.mp3",   format = "mp3")    