# 任务二笔记

```
os.makedirs(test_path, exist_ok=True)
```

这行代码会创建一个名为`train_folder`的文件夹。如果该文件夹已存在，`exist_ok=True`表示不会引发错误，即如果文件夹已存在就不会再次创建。

---

```
marvel_path = os.path.join(data_path, marvel_list)
```

os.path.join() 用于将两个路径合并成一个完整的路径。

---

```
image_path = [f for f in os.listdir(marvel_path) if f.endswith(".jpg")]
```

f.endswith(".jpg") 用于提取所有后缀为jpg的图片

---

```
train_images, temp_images = train_test_split(image_path, test_size=0.2, random_state=42)
```

是sklearn用来划分数据集的函数，第一个参数是路径，第二个是划分出来的percent，第三个是"种子"，使用固定种子，利于复刻

返回值有两个，分别是划分后的训练集和剩余的图像文件列表

---

```
shutil.copy(image_path, os.path.join(train_path, image))
```

复制文件函数，分别传源路径和目标路径

---

---

**计算灰度图像**：

把彩色图像转成灰度图像。

```
cv2.imread(img_path)
```

opencv中 用于读取图片的函数，传入图片路径

---

RGB图片有三个通道（R、G、B）,用光度感知比例(0.3, 0.59, 0.11)可以将其转换成灰度图片
---

```
# 转换为灰度图
row, col, channel = img.shape
gray_img = numpy.zeros((row, col)) # 创建一个空白的灰度图

for i in range(row):
    for j in range(col):
        gray_img[i, j] = 0.3 * img[i, j, 0] + 0.59 * img[i, j, 1] + 0.11 * img[i, j, 2] # 灰度图的计算公式
```

---

```
cv2.waitKey()
```

等待键盘操作

---

```
cv2.imshow("gray_img", gray_img.astype("uint8"))
```

打开图片，后面要加编码的参数

---

---

```
data = np.load()
```

加载numpy数据(.npz)

---

