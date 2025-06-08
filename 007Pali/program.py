import MyModule

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

text_result = ""
for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
    text_id = splitLine[0]
    text = splitLine[1]

    text = MyModule.romanpali_to_thai(text)
    text_result = text_result + text_id + "\t" + text + "\n"
    print(text_id, text)

result_file.write (text_result.strip())    