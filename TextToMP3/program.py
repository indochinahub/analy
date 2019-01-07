# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
from gtts import gTTS
import os
import time

def clearBracket(words) :
    #print(words)
    i = 0
    while 1 :
        start = words.find("(")
        end  = words.find(")") +1
        words = words.replace( words[start:end], "")
        #print(words)
        i = i+1
        if i > 6 :
           break
    return words


source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    number = splitLine[0]
    words  = clearBracket(splitLine[1])

    tts = gTTS(text=words, lang='vi')
    tts.save("VN112-DRILL-"+number.strip()+".mp3" )
    print( line, words )

# Lang = vi, ja, en,km    
#tts.save("Tribes-"+splitLine[0].strip()+".mp3" )
# tts.save("HellonWheel-"+splitLine[0].strip()+".mp3" )
# tts.save("GOT5-"+splitLine[0].strip()+".mp3" )
# tts.save("VN201T-"+splitLine[0].strip()+".mp3" )
# tts.save("VN109T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH112T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH202T-ReadingPractice-"+splitLine[0].strip()+".mp3") สำหรับหนังสือหลักการอ่าน
# tts.save("KH202T-Reading-"+splitLine[0].strip()+".mp3")
# tts.save("KH205T-"+splitLine[0].strip()+".mp3" )
# tts.save("VN111-"+splitLine[0].strip()+".mp3" )