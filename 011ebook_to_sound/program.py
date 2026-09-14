# main.py
import mymodule

 
with open("source.txt", encoding='utf-8', mode='r') as file:
    text = file.read()

result_file = open('result.txt', encoding='utf-8', mode='w')    

arr_group_of_line = mymodule.get_group_of_line(text)

arr_group = []
for group in arr_group_of_line:
    arr_sentence = group.split('\n')
    if len(arr_sentence) < 2:
        print ("Error: len()< 2 : " + arr_sentence[0] + '\n*********')
    else:
        #print(arr_sentence)
        arr_group.append(arr_sentence)

output_text = ""
output_text2 = ""
for group in arr_group:
    topic = group[0]

    group_text = ""
    for i in range(len(group)):
        if i > 0:
            group_text = group_text + " " + str(i) + ") " + group[i]
            output_text2 = output_text2 + topic +  "\t" + group[i] + "\n"
    
    output_text = output_text + topic + "\t" + group_text + "\n"

print(output_text)
result_file.write (output_text.strip()  +"\n******\n" + output_text2.strip())
#result_file.write (output_text2.strip())
result_file.close ()




    


