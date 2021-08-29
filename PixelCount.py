import os
from PIL import Image
from os import listdir
from os.path import isfile, join
directory = r'H:\HW10m96dem315bedhwM024Final3\animation'
os.chdir(directory)
file1 = open(r"H:\HW10m96dem315bedhwM024Final3\area.txt", "w+")
for filename in sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime): # list files in through directory file
         for wetCount in directory: #loops through directory files
            im = Image.open(os.path.join(directory, filename)) # assigns image file to variable "im"

            dry = 0
            wet = 0

            for pixel in im.getdata(): # iterates through a single image for pixel count
                if pixel == (0, 0, 0, 0) : # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                    dry += 1
                else:
                    wet += 1
            #print('wet='+str(wet)) for checking code in viusal studio code
            print(wet)
            file1.write('\n' + str(wet))
            break







