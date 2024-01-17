from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

img_path = "../1.15Dataset/Datasets/train/ants_image/5650366_e22b7e1065.jpg"
img = Image.open(img_path)

trans_tensor = transforms.ToTensor()
tensor_image = trans_tensor(img)

writer = SummaryWriter("logs")
writer.add_image("tensor_image", tensor_image)

writer.close()