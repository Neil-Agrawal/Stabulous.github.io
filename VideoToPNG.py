import cv2
import config
import shutil
import os


def Convert(video_loc,mystatus):
    KPS = 24# Target Keyframes Per Second
    VIDEO_PATH = video_loc
    
    #Clean directory
    if (os.path.isdir(config.UserConvert_Location)):
        shutil.rmtree(config.UserConvert_Location)
    os.makedirs(config.UserConvert_Location)
    IMAGE_PATH = f"{config.UserConvert_Location}/"
    
    #Setup
    EXTENSION = ".png"
    cap = cv2.VideoCapture(VIDEO_PATH)
    fps = round(cap.get(cv2.CAP_PROP_FPS))

    hop = round(fps / KPS)
    curr_frame = 0
    
    
    #Convert to frames
    mystatus.setStatus("Converting video to frames")
    while(True):
        ret, frame = cap.read()
        if not ret: 
            break
        if curr_frame % hop == 0:
            name = IMAGE_PATH+str(curr_frame) + EXTENSION
            cv2.imwrite(name, frame)
            curr_frame += 1
    cap.release()