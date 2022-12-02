import cv2
import numpy as np
import glob
import os
import config

#Organize file
def OrganizeArrayByNumber(array):
    swap=True
    while(swap==True):
        swap=False
        for i in range(len(array)-1):
            temp=array[i].split(".")[0]
            
            num=int(temp)
            temp=array[i+1].split(".")[0]
            nextnum=int(temp)
            if num>nextnum:
                swap=True
                array[i],array[i+1]=array[i+1],array[i]
    return array

def Convert(video_dir,video_name,mystatus):
    mystatus.setStatus("Convert frames to video...")
    img_array = []
    myfile=os.listdir(config.UserResultsLocation)
    myfile=OrganizeArrayByNumber(myfile)
    for i in range(len(myfile)):
        filename=myfile[i]
        image = f"{config.UserResultsLocation}/" + filename
        img = cv2.imread(image)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    
    
    
    out = cv2.VideoWriter(f'{video_dir}Stable_{video_name}',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
     
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
