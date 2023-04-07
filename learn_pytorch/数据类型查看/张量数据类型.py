import numpy as np
import torch

print(torch.tensor(1.))  # 创建一个0维张量，loss常用此表示

print(torch.tensor(1.3))  # 1.3是0维
print(torch.tensor([1.3]))  # [1.3]是一维

# 检查tensor的shape（dim 0,也被称为标量）
a = torch.tensor(2.2)
print(a.shape)  # 返回的是一个空的list，但是a并不是list，只是表示一个空的list的大小
print(len(a.shape))  # a.dim也行，告诉你a的维度
print(a.size())

print("---------我是分界线---------")

# dim 1，也被称为张量，经常用来表示偏置（bias）与btach为1的神经网络的输入也可以用dim为1的tensor表示
print(torch.tensor([1.1]))  # 加上[]之后表示dim=1的张量
print(torch.tensor([1.1, 2.2]))  # dim=2的张量
print(torch.FloatTensor(1))
print(torch.FloatTensor(2))

data = np.ones(2)
print(data)
print(torch.from_numpy(data))

print("---------我是分界线---------")

# dim 2 ，经常用来表示带有batch的线性网络的输入
a = torch.randn(2, 3)  # 随机产生一个2*3矩阵（randn：随机正态分布）
print(a)
print(a.shape)
print(a.size(0))  # 如果参数为空，size就会返回torch.Size([2, 3])，参数为0就返回[2,3]的第0各元素，也就是几行
print(a.size(1))  # 返回几列
print(a.shape[1])

print("---------我是分界线---------")

# dim 3
a = torch.rand(1, 2, 3)  # rand：随机均匀分布（0~1）
print(a)
print(a.shape)
print(a[0])
print(list(a.shape))  # 用list方法将torch.size转为list
