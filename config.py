import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "frames/train"
VAL_DIR = "frames/val"
LEARNING_RATE = 2e-4
BATCH_SIZE = 16
NUM_WORKERS = 0
IMAGE_SIZE = 256
CHANNELS_IMG = 3
L1_LAMBDA = 100
LAMBDA_GP = 10
NUM_EPOCHS = 249
NUM_EPOCHS = 100
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_DISC = "disc.pth.tar"
CHECKPOINT_GEN = "gen.pth.tar"
UserIMG_Location="D:/AIM_GAN_Model/UnstableFrames/video0/"
VideoLocTest=r"D:\AIM_GAN_Model\PersonalTest\unstable\1.avi"
UserConvert_Location="D:/AIM_GAN_Model/YoutubeTest/VideoStablizer/User_Convert"
UserResultsLocation="D:/AIM_GAN_Model/YoutubeTest/VideoStablizer/User_results"

both_transform = A.Compose(
    [A.Resize(width=256, height=256),], additional_targets={"image0": "image"},
)

transform_only_input = A.Compose(
    [
        A.HorizontalFlip(p=0.5),
        A.ColorJitter(p=0.2),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
        ToTensorV2(),
    ]
)

transform_only_mask = A.Compose(
    [
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
        ToTensorV2(),
    ]
    )