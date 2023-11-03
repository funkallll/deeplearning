from torchsummary import summary  # 使用torchsummary测试网络结构
from unet import UNet             # 以unet为例
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(3, 1).to(device)     # 输入unet网络参数class UNet(nn.Module):def __init__(self, n_channels, n_classes, bilinear=False):
summary(model, input_size=(3, 572, 572))
