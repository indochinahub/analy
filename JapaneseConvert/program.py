# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
from gtts import gTTS
import os
import romkan

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    hiragana = romkan.to_hiragana(splitLine[1])
    result_file.write( splitLine[0]+ '\t' + splitLine[1]+ '\t' + hiragana + '\n')    
    
    tts = gTTS(text= hiragana , lang='ja')
    tts.save("JP103-words-"+splitLine[0].strip()+".mp3" )   
    print( splitLine )    

    
    
    
    
#Lang = vi, ja, en
    
    
    
    