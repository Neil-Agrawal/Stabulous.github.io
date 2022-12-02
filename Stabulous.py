import os
import VideoToPNG
import config
import utils
import train
import PNGToVideo

def main(video_loc,mystatus):
    #Get file from user
    if(not os.path.isfile(video_loc)):
        return "File does not exist error"
    video_loc=video_loc.replace("\\","/")
    video_directory=video_loc
    i=1
    video_name=""
    while (len(video_loc)-i>0):
        char=video_loc[len(video_directory)-i]
        if(char!="/"):
            video_name=char+video_name
            i=i+1
        else:
            break
    video_directory=video_directory.replace(video_name, "")
    try:
        #Convert file into png frames
        VideoToPNG.Convert(video_loc,mystatus)
        train.Create_Stable(mystatus)
    except Exception as e:
        return f"Error: {e}"
    PNGToVideo.Convert(video_directory,video_name,mystatus)
    return "Done"

        


if __name__ == "__main__":
    video_loc=config.VideoLocTest
    #Status for website to display
    mystatus=utils.Status()
    mystatus.setStatus("Starting...")
    mystatus.setStatus(main(video_loc,mystatus))