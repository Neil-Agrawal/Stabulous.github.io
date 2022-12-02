from PIL import Image
import os

#Organize file
def OrganizeArrayByNumber(array):
    swap=True
    while(swap==True):
        swap=False
        for i in range(len(array)-1):
            num=int(array[i].split(".")[0])
            nextnum=int(array[i+1].split(".")[0])
            if num>nextnum:
                swap=True
                array[i],array[i+1]=array[i+1],array[i]
    return array

#Read the two images
root1=os.listdir('D:/AIM_GAN_Model/UnstableFrames/video14/')
root2=os.listdir('D:/AIM_GAN_Model/StableFrame/video14/')

root1=OrganizeArrayByNumber(root1)
root2=OrganizeArrayByNumber(root2)

if len(root1)<=len(root2):
    root_length=len(root1)
    root=root1
    not_root_length=len(root2)
    rev_root=root2
else :
    root_length=len(root2)
    root=root2
    not_root_length=len(root1)
    rev_root=root1

    

for i in range(root_length):
    print(f"{i+1}/{root_length}")
    print(root1[i],root2[i])
    image1 = Image.open(f'D:/AIM_GAN_Model/UnstableFrames/video14/{root1[i]}')
    image2 = Image.open(f'D:/AIM_GAN_Model/StableFrame/video14/{root2[i]}')

#    resize, first image
    image1 = image1.resize((426, 240))
    image2 = image2.resize((426, 240))
    image1_size = image1.size
    image2_size = image2.size
#   combine
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
#   Save
    new_image.save(f"D:/AIM_GAN_Model/PersonalTest/val/14_{root[i]}","PNG")
