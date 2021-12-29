import os
from fpdf import FPDF

image_path = os.getcwd() + "\\image\\"

init_y_for_image = 15
image_offset = 45

pdf = FPDF('P','mm', 'A4')
pdf.set_font('helvetica', '', 14)
pdf.set_text_color(220, 50, 50)

#pdf.set_auto_page_break(auto = 1)

for i in range(1, 2):

    pdf.add_page()
    pdf.image( image_path + '0010.jpg', 0, init_y_for_image, 80, 40)
    pdf.image( image_path + '0020.jpg',0, init_y_for_image + image_offset , 80, 40)
    pdf.image( image_path + '0010.jpg',0, init_y_for_image + (image_offset*2) , 80, 40)
    pdf.image( image_path + '0020.jpg',0, init_y_for_image + (image_offset*3) , 80, 40)
    pdf.image( image_path + '0010.jpg',0, init_y_for_image + (image_offset*4) , 80, 40)
   
   
    pdf.set_xy( 65, init_y_for_image )
    text = '1. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x\n'
    text = text + '2. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'
    pdf.multi_cell( 0, 10, text, border = 1,  fill = False, ln = 1)
    
    pdf.set_xy( 65, init_y_for_image + image_offset )
    text = '1. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x\n'
    text = text + '2. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'
    pdf.multi_cell( 0, 10, text, border = 1,  fill = False, ln = 1)


    pdf.set_xy( 65, init_y_for_image + (image_offset * 2) )
    text = '1. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x\n'
    text = text + '2. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'
    pdf.multi_cell( 0, 10, text, border = 1,  fill = False, ln = 1)
    
    pdf.set_xy( 65, init_y_for_image + (image_offset * 3) )
    text = '1. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x\n'
    text = text + '2. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'
    pdf.multi_cell( 0, 10, text, border = 1,  fill = False, ln = 1)

    pdf.set_xy( 65, init_y_for_image + (image_offset * 4) )
    text = '1. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x\n'
    text = text + '2. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x'
    pdf.multi_cell( 0, 10, text, border = 1,  fill = False, ln = 1)

pdf.output('001.pdf')


#pdf.set_auto_page_break(auto=True, margin = 30)






#for i in range(1, 200):
#    pdf.cell(0, 15, f'This is line (i) :D', ln = True)


