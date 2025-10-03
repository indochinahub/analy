import cv2
import os

# Load the image
# img = cv2.imread("01.png")

# Define the desired dimensions (width, height)
# (250, 166), 

#image_path = r'C:\Users\wittaya\Desktop\picture'
image_path = r'C:\Users\wittaya\Downloads'

for folder, subfolder, files in os.walk(image_path) : 
    for file in files:
        full_pathname = image_path + '\\' + file
        new_full_pathname = image_path + '\\' + "a_"+ file 
        #old_full_pathname = image_path + '\\' + "x_"+ file
        old_full_pathname = image_path + '\\' + file
        img = cv2.imread(full_pathname)
        
        
        
        # Crop the image using slicing
        x_start, y_start, x_end, y_end = 110, 180, 950, 860  # Adjust as needed
        img = img[y_start:y_end, x_start:x_end]
        
        desired_width = 300
        desired_height = 242
        img = cv2.resize(img, (desired_width, desired_height))
        
        cv2.imwrite(new_full_pathname, img)
        os.rename(full_pathname, old_full_pathname)
        print (full_pathname)
        print (new_full_pathname)