# -*- coding: utf-8 -*-


from google.cloud import translate
import unicodedata

import io
source_file = open('source.txt', mode='r')
#result_file = open('result.txt', mode='w')
result_file = io.open('result.txt', mode='w', encoding='utf-8')


client = translate.Client(target_language='en')

for line in source_file :
    line = line.strip()
    line = line.split("\t")
    result = client.translate(line[1], source_language='vi')
    result['translatedText'] = result['translatedText'].replace('&quot;', '\"')
    result['translatedText'] = result['translatedText'].replace('&#39;', '\'')
    result['translatedText'] = result['translatedText'].replace(';', ':')
    print(line[0], type(result['translatedText']))
    result_file.write(line[0] + "\t" + result['translatedText'] + "\n")

result_file.close()


# Lang = vi, ja, en,km    
# tts.save("VN201T-"+splitLine[0].strip()+".mp3" )
# tts.save("VN109T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH112T-words-"+splitLine[0].strip()+".mp3" )
# tts.save("KH202T-ReadingPractice-"+splitLine[0].strip()+".mp3") สำหรับหนังสือหลักการอ่าน
# tts.save("KH202T-Reading-"+splitLine[0].strip()+".mp3")