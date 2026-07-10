# -*- coding: utf-8 -*-

#
# You need to fill the blank line at the end of the source file.
#
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
import time

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

# Lang = vi, ja, en, km, zh-cn, ko, th
lang_source = "en"
lang_target = "vi"

MyTranslate = GoogleTranslator(source= lang_source, target= lang_target)

result_file.write ("")
result_file.close ()
result_file = open('result.txt', encoding='utf-8', mode='a')
for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    
    text_id = splitLine[0]
    text = splitLine[1]
    
    # Lang = vi, ja, en, km, zh-cn, ko, th
    #tts = gTTS(text , lang='en')
    #tts.save(""+splitLine[0].strip()+".mp3" )
    
    #translator.translate( text, src='th')
    #MyTranslate = GoogleTranslator(source= lang_source, target= lang_target)
    tranlated_text  = MyTranslate.translate(text)
	
    print( text_id + "\t" + text )
    result_file.write (text_id + "\t" +  tranlated_text  + "\n")
    
    time.sleep(1)