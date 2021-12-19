import os
import uuid
from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def zero_fill(number, length):
    str_number = str(number)
    while len(str_number) < length:
        str_number = "0"+ str_number

    return str_number


img_path = os.getcwd() + "\\image\\"

images = convert_from_path(
                    pdf_path = 'source.pdf',
                    poppler_path = r"D:\programfiles\poppler-21.11.0\Library\bin",
                    #output_folder= img_path,
                    fmt="jpg",
                    size = (800, None),
                )

i = 1
for image in images:

    image.save( img_path + zero_fill(i, 3)  + '.jpg')
    i = i + 1


