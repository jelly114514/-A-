import os
from sklearn.model_selection import train_test_split
import shutil

data_path = "./data/marvel"
to_path = "./data/data"

# 创建文件夹
train_path = os.path.join(to_path, "train")
val_path = os.path.join(to_path, "val")
test_path = os.path.join(to_path, "test")
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

marvel_lists = os.listdir(data_path)

# 划分数据集
for marvel_list in marvel_lists:
    marvel_path = os.path.join(data_path, marvel_list)
    image_path = [f for f in os.listdir(marvel_path) if f.endswith(".jpg")]
    train_images, temp_images = train_test_split(image_path, test_size=0.2, random_state=42)
    val_images, test_images = train_test_split(temp_images, test_size=0.5, random_state=42)  # 划分训练集测试集和验证集

    # 复制图片
    train_folder = os.path.join(train_path, marvel_list)
    os.makedirs(train_folder, exist_ok=True)
    val_folder = os.path.join(val_path, marvel_list)
    os.makedirs(val_folder, exist_ok=True)
    test_folder = os.path.join(test_path, marvel_list)
    os.makedirs(test_folder, exist_ok=True)
    for image in train_images:
        image_path = os.path.join(marvel_path, image)
        shutil.copy(image_path, os.path.join(train_folder, image))
    for image in val_images:
        image_path = os.path.join(marvel_path, image)
        shutil.copy(image_path, os.path.join(val_folder, image))
    for image in test_images:
        image_path = os.path.join(marvel_path, image)
        shutil.copy(image_path, os.path.join(test_folder, image))

