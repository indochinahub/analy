import sys
sys.path.append("../")

#from MyModule import PaliModule

from gtts import gTTS
import os
import time

thai_file = open('thai.txt', encoding='utf-8', mode='r')


for line in thai_file :
    line = line.strip()
    splitLine = line.split("\t")
    
    text_id = splitLine[0]
    text = splitLine[1]
    
    text = text.replace("[newline]"," ")
    
    # Lang = vi, ja, en, km, zh-cn, ko, th
    tts = gTTS(text , lang='th')
    tts.save(""+splitLine[0].strip()+".mp3" )
	
    print( text_id + "\t" + text )
    
    time.sleep(2)