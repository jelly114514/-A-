# Tensorboard

可以用来画图，是可视化机器学习模型训练过程和结果的工具，可以直观的看到loss的下降

打开:（终端）

​	tensorboard --logdir=事件文件所在文件夹名

修改端口：

​	ttensorboard --logdir=事件文件所在文件夹名  --port=新的端口



```writer.add_image("tag", image_array, 1[global_step])```

**从PIL到numpy，需要在add image()中指定shape中每一个数字/维表示的含义，即：**

**如果图片的shape不是(3~通道数~, H~高度~ , W~宽度~)，  则要加个参数dataformats，如：**,

```writer.add_image("test", image_array,1 ,dataformats='HWC')```

C是channel 通道数

W是weight 宽度

H是hight 高度





**label(图像标题记得换)**

**writer.add_scalar("label",y, x)是先y后x**

**__路径一定不可以含中文和空格__**

