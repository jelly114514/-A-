from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "../1.15Dataset/Datasets/train/ants_image/5650366_e22b7e1065.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(img_array.shape)
writer.add_image("test", img_array, 1, dataformats='HWC')

for i in range(100):
    writer.add_scalar("y = 3x", 3*i, i)

writer.close()