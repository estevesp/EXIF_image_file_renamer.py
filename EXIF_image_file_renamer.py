#Package Imports
import os
import collections
from PIL import Image

#Functions Definition

#Function to clear the screen
clear = lambda: os.system('cls')

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

#Function that returns the Date Taken Timestamp of any given filename
def get_date_taken(path):                     
    return Image.open(path)._getexif()[36867]

#Function to parse the EXIF timestamp and convert to Google Photos timestamp format

#Parse and append JPG extension to argument
def timestamp_with_jpg(timestamp):
    return timestamp.replace(":","").replace(" ","_") + ".jpg"

#Class that represents the pictures being processed
class MyPicture ():
    def __init__(self, file_name, date_taken, index):
        self.file_name = file_name
        self.date_taken = date_taken
        self.index = index

#Variables Definitions
IMAGES_PATH = "C:\\Users\\estevesp\\Desktop\\IMG"
IMAGES_LIST = os.listdir(IMAGES_PATH)
MyPictureList = []
MyDateTakenList = []
index = 0
counter = 1

#Main 
os.system('cls')
for CURRENT_FILE in IMAGES_LIST:
    FULL_IMAGE_FILE_NAME = IMAGES_PATH + "\\" + CURRENT_FILE
    MyPictureList.append(MyPicture(FULL_IMAGE_FILE_NAME,get_date_taken(FULL_IMAGE_FILE_NAME), index))
    index += 1
    
    
MySortedPictureList = sorted(MyPictureList, key=lambda x: x.date_taken)

for Picture in MySortedPictureList:
    
    try:
        rename_file(Picture.file_name, IMAGES_PATH + "\\" + timestamp_with_jpg(Picture.date_taken))
        counter = 1
    except:
        Picture.date_taken = Picture.date_taken + "_" + format(counter, "03d")
        rename_file(Picture.file_name, IMAGES_PATH + "\\" + timestamp_with_jpg(Picture.date_taken))
        counter += 1
