from torch.utils.data import Dataset
from PIL import Image
import os

class My_dataset(Dataset):

    def __init__(self, root_dir, label_dir) -> None:
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.image_path = os.listdir(self.path)

    def __getitem__(self, index):
        image_name = self.image_path[index]
        img_item_path = os.path.join(self.root_dir, self.label_dir, image_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        
        return img, label

    def __len__(self):
        return len(self.image_path)

root_dir = "Pytorch_learning\\Datasets\\train"
ants_label_dir = "ants_image"
ants_dataset = My_dataset(root_dir, ants_label_dir)
bees_label_dir = "bees_image"
bees_dataset = My_dataset(root_dir, bees_label_dir)

#可以通过+来合并数据集
train_dataset = ants_dataset + bees_dataset
print(len(bees_dataset))
print(len(ants_dataset))
print(len(train_dataset))
img, label = train_dataset[124]
img.show()



"""是注释"""