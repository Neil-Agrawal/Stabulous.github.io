import torch
import config
from torchvision.utils import save_image
from PIL import Image
import os
import numpy as np


class Status:
    def __init__(self):
        self.status="none"
    def setStatus(self,val):
        self.status=val
        print(self.status)

def save_some_examples(gen, val_loader, epoch, folder):
    temp=iter(val_loader)
    x, y = next(temp)
        
    x, y = x.to(config.DEVICE), y.to(config.DEVICE)
    gen.eval()
    with torch.no_grad():
        y_fake = gen(x)
        y_fake = y_fake * 0.5 + 0.5  # remove normalization#
        save_image(y_fake, folder + f"/y_gen_{epoch}.png")
        save_image(x * 0.5 + 0.5, folder + f"/input_{epoch}.png")
        if epoch == 1:
            save_image(y * 0.5 + 0.5, folder + f"/labVAL_DIRel_{epoch}.png")
    gen.train()
    
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

def save_results(gen, val_loader, img_num, folder):
    temp=iter(val_loader)
    x,y=temp
        
    x, y = x.to(config.DEVICE), y.to(config.DEVICE)
    gen.eval()
    with torch.no_grad():
        y_fake = gen(x)
        y_fake = y_fake * 0.5 + 0.5  # remove normalization#
        save_image(y_fake, folder + f"/{img_num}.png")

        



def save_checkpoint(model, optimizer, filename="my_checkpoint.pth.tar"):
    print("=> Saving checkpoint")
    checkpoint = {
        "state_dict": model.state_dict(),
        "optimizer": optimizer.state_dict(),
    }
    torch.save(checkpoint, filename)


def load_checkpoint(checkpoint_file, model, optimizer, lr):
    print("=> Loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location=config.DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])

    # If we don't do this then it will just have learning rate of old checkpoint
    # and it will lead to many hours of debugging \:
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr

def user_input(file_location):
    image1 = Image.open(f'{file_location}')
    image2 = Image.open(f'{file_location}')

#    resize, first image
    image1 = image1.resize((426, 240))
    image2 = image2.resize((426, 240))
    image1_size = image1.size
#   combine
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    
    #Data appropiate
    image = np.array(new_image)
    
    input_image = image[:, :426, :]
    target_image = image[:, 426:, :]

    augmentations = config.both_transform(image=input_image, image0=target_image)
    input_image = augmentations["image"]
    target_image = augmentations["image0"]

    input_image = config.transform_only_input(image=input_image)["image"]
    target_image = config.transform_only_mask(image=target_image)["image"]

    return input_image, target_image