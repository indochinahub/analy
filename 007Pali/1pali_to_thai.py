import sys
sys.path.append("../")

from MyModule import PaliModule

pali_file = open('pali.txt', encoding='utf-8', mode='r')
thai_file = open('thai.txt', encoding='utf-8', mode='w')


text_result = ""
for line in pali_file :
    line = line.strip()
    splitLine = line.split("\t")
    text_id = splitLine[0]
    text = splitLine[1]

    print(text_id, text)
    text = PaliModule.romanpali_to_thai(text)
    text_result = text_result + text_id + "\t[" + text + "]\n"
    

thai_file.write (text_result.strip())    
