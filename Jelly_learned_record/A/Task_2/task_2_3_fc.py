import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
import numpy as np
from torch.utils.tensorboard import SummaryWriter

# 加载 .npz 文件
datas = np.load("./data/data/datasets.npz", allow_pickle=True)
# 获取类型
print(datas.files)
print(type(datas['data']))

# 获取数据
features = datas['data'][:, :3]  # 获取每个样本的前三个元素
labels = datas['data'][:, 3:]    # 获取每个样本的第四个元素

# 划分数据集
train_features, test_features = (
    train_test_split(features, test_size=0.2, random_state=42))
train_labels, test_labels = (
    train_test_split(labels, test_size=0.2, random_state=42))


# 转换为 PyTorch Tensor
train_features = torch.Tensor(train_features)
test_features = torch.Tensor(test_features)
train_labels = torch.Tensor(train_labels)
test_labels = torch.Tensor(test_labels)

# 创建 PyTorch DataLoader
train_dataset = TensorDataset(train_features, train_labels)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# 创建全连接神经网络
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建模型、损失函数和优化器
input_size = 3  # 输入特征的维度
hidden_size = 128  # 隐藏层维度
output_size = 2  # 输出的维度
model = SimpleNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.0001, momentum=0.8)

# 使用 TensorBoard
writer = SummaryWriter(log_dir='./logs')

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    for batch_idx, (batch_features, batch_labels) in enumerate(train_loader):
        optimizer.zero_grad()
        outputs = model(batch_features)
        loss = criterion(outputs, batch_labels)
        loss.backward()
        optimizer.step()

        # 记录损失值到 TensorBoard
        global_step = len(train_loader) * epoch + batch_idx
        writer.add_scalar('loss图', loss.item(), global_step)

# 在测试集上进行测试
test_dataset = TensorDataset(test_features, test_labels)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

model.eval()
total_loss = 0

with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        outputs = model(batch_features)
        loss = criterion(outputs, batch_labels)
        total_loss += loss.item()

# 计算平均测试损失
avg_test_loss = total_loss / len(test_loader)
print(f'Average Test Loss: {avg_test_loss}')

# 关闭 TensorBoard 写入
writer.close()