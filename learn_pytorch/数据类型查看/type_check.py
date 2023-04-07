import torch

a = torch.randn(2, 3)  # 创建一个二维tensor
print(a.type())  # 查看type类型
print(type(a))  # 也是查看参数类型的方法之一，因为获得的信息比较少所以用得少
print(isinstance(a, torch.FloatTensor))  # 参数合法化检验


