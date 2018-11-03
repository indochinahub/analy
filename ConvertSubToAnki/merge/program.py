# -*- coding: utf-8 -*-

#
# You need to check if the two files has same amount of lines.
#

source_file1 = open('en.txt', encoding='utf-8', mode='r')
source_file2 = open('vn.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')

i = 0
front = []
for line in source_file1 :
    front.append(line.strip(' \t\n\r,'))
    i = i +1 
front_number = i

i = 0
for line in source_file2 :
    back = line.strip(' \t\n\r,')
    result_file.write( front[i] + " ; " + back + "\n" )
    i = i +1 
back_number = i

print ( "front : " + str( front_number)  + "\nback : " + str(back_number))



result_file.close()    
