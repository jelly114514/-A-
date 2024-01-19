import cv2
import numpy

# 读取图片
img_path = "./data/marvel/doctor strange/pic_268.jpg"
img = cv2.imread(img_path)
# 获取图片的宽高
print(img.shape)

# 转换为灰度图
row, col, channel = img.shape
gray_img = numpy.zeros((row, col)) # 创建一个空白的灰度图
gray_mean = 0

for i in range(row):
    for j in range(col):
        gray_img[i, j] = 0.3 * img[i, j, 0] + 0.59 * img[i, j, 1] + 0.11 * img[i, j, 2] # 灰度图的计算公式
        gray_mean += gray_img[i, j]

# 使用numpy公式计算灰度图像的均值和方差
gray_array = numpy.array(gray_img)
mean_value = numpy.mean(gray_array)
variance_value = numpy.mean((gray_array - mean_value) ** 2)
print("numpy计算灰度图像方差:", variance_value)

# 手搓计算灰度图像的均值和方差
gray_mean/= (row * col)
my_variance = 0
for i in range(row):
    for j in range(col):
        my_variance += (gray_img[i, j] - gray_mean) ** 2
my_variance /= (row * col)
print("手搓计算灰度图像方差:", my_variance)

# 保存图片
cv2.imwrite("gray_img.jpg", gray_img)

# 显示图片
cv2.imshow("gray_img", gray_img.astype("uint8"))
cv2.waitKey()
