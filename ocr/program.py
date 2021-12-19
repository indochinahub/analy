from PIL import Image
import pytesseract
import os

def zero_fill(number, length):
    str_number = str(number)
    
    while len(str_number) < length:
        str_number = "0"+ str_number

    return str_number

start_page  = 2
end_page = 3

img_path = os.getcwd() + "\\image\\"
result_file = open('result.txt', encoding='utf-8', mode='w')

pytesseract.pytesseract.tesseract_cmd = 'D:\\programfiles\\Tesseract-OCR\\tesseract.exe'

text = ""
for page_number in range( start_page, end_page + 1):
    page_number = zero_fill(page_number, 3)
    
    image_filename = page_number + ".jpg"
    img = Image.open( img_path + image_filename )

    text = text + "[ Page :: " + page_number +" ]\n"
    text = text + pytesseract.image_to_string(  img , lang='vie') + "\n"

    print(page_number)


result_file.write( text )