# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
from gtts import gTTS
import os

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    tts = gTTS(text=splitLine[1], lang='en')
    print ("Hello")
    tts.save("GOT-"+splitLine[0].strip()+".mp3" )
    print( splitLine )

# Lang = vi, ja, en,km    
# tts.save("GOT-"+splitLine[0].strip()+".mp3" )
# tts.save("VN201T-"+splitLine[0].strip()+".mp3" )
# tts.save("VN109T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH112T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH202T-ReadingPractice-"+splitLine[0].strip()+".mp3") สำหรับหนังสือหลักการอ่าน
# tts.save("KH202T-Reading-"+splitLine[0].strip()+".mp3")