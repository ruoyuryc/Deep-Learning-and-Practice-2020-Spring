import torch
import torch.nn as nn

import torchvision

def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.normal_(m.weight, 0.0, 0.02)
    elif classname.find('BatchNorm2d') != -1:
        nn.init.normal_(m.weight, 1.0, 0.02)
        nn.init.constant_(m.bias, 0.0)

def make_grid(images, epoch, batch, acc):
    grid = torchvision.utils.make_grid((images + 1) / 2, nrow=8)
    torchvision.utils.save_image(grid, f'plot/Epoch-{epoch}-{batch}-{acc}.png')

