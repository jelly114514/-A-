from torch.utils.data import Dataset
from PIL import Image
import os
#自己定义的类 
class My_dataset(Dataset):
    #初始化
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

#获取数据集
root_dir = "Pytorch_learning\\Datasets\\train"
ants_label_dir = "ants_image"
ants_dataset = My_dataset(root_dir, ants_label_dir)
bees_label_dir = "bees_image"
bees_dataset = My_dataset(root_dir, bees_label_dir)
train_dataset = ants_dataset + bees_dataset

#写标签
root_dir = 'Datasets/train'
target_dir = 'ants_image'
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split('_')[0]
out_dir = 'ants_label'
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir, out_dir,"{}.txt".format(file_name)),'w') as f:
        f.write(label)
#写标签
root_dir = 'Datasets/train'
target_dir = 'bees_image'
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split('_')[0]
out_dir = 'bees_label'
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir, out_dir,"{}.txt".format(file_name)),'w') as f:
        f.write(label)

#测试
print(len(bees_dataset))
print(len(ants_dataset))
print(len(train_dataset))
img, label = train_dataset[124]
img.show()
