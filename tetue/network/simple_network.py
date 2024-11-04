import torch
import torch.nn as nn
import torch.nn.functional as F

from tetue.features import MOVE_PLANES_NUM, MOVE_LABELS_NUM

INPUT_CHANNELS = 104


class ResNetBlock(nn.Module):
    def __init__(self, channels):
        super(ResNetBlock, self).__init__()
        self.conv1 = nn.Conv2d(
            channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(
            channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = F.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        return F.relu(out + x)


class SimpleNetwork(nn.Module):
    def __init__(self):
        super(SimpleNetwork, self).__init__()
        num_filters = 192
        blocks = 10
        self.conv1 = nn.Conv2d(
            in_channels=INPUT_CHANNELS, out_channels=num_filters, kernel_size=3, padding=1, bias=True)
        self.norm1 = nn.BatchNorm2d(num_filters)

        # resnet blocks
        self.blocks = nn.Sequential(
            *[ResNetBlock(num_filters) for _ in range(blocks)])

        # policy head
        self.policy_conv = nn.Conv2d(
            in_channels=num_filters, out_channels=MOVE_PLANES_NUM, kernel_size=1, bias=False)
        # self.policy_bias = Bias(MOVE_LABELS_NUM)

        # value head
        self.value_conv1 = nn.Conv2d(
            in_channels=num_filters, out_channels=MOVE_PLANES_NUM, kernel_size=1, bias=False)
        self.value_norm1 = nn.BatchNorm2d(MOVE_PLANES_NUM)
        self.value_fc1 = nn.Linear(MOVE_LABELS_NUM, 256)
        self.value_fc2 = nn.Linear(256, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.norm1(x)
        x = F.relu(x)

        x = self.blocks(x)

        # policy head
        policy = self.policy_conv(x)
        policy = torch.flatten(policy, 1)
        # FIXME: Add bias

        # value head
        value = self.value_conv1(x)
        value = self.value_norm1(value)
        value = F.relu(value)
        value = torch.flatten(value, 1)
        value = self.value_fc1(value)
        value = F.relu(value)
        value = self.value_fc2(value)
        return policy, value
