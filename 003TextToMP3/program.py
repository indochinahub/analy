# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
from gtts import gTTS
import os
import time

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    
    text_id = splitLine[0]
    text = splitLine[1]
    
    text = text.replace("[newline]"," ")
    
    # Lang = vi, ja, en, km, zh-cn, ko, th, la(Latin),  my (Myanmar), id(Indonesian), lv(Latvia)
    tts = gTTS(text , lang='th')
    tts.save(""+splitLine[0].strip()+".mp3" )
	
    print( text_id + "\t" + text )
    
    time.sleep(2)

