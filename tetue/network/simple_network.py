import torch
import torch.nn as nn
import torch.nn.functional as F

from tetue.features import MOVE_PLANES_NUM, MOVE_LABELS_NUM

INPUT_CHANNELS = 104


class SimpleNetwork(nn.Module):
    def __init__(self):
        super(SimpleNetwork, self).__init__()
        num_filters = 192
        self.conv1 = nn.Conv2d(
            in_channels=INPUT_CHANNELS, out_channels=num_filters, kernel_size=3, padding=1, bias=True)
        # self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

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
        # Apply convolution, ReLU, and pooling
        x = self.conv1(x)
        x = F.relu(x)
        # x = self.pool()

        # policy head
        policy = self.policy_conv(x)
        # policy = self.policy_bias(torch.flatten(policy, 1))
        policy = torch.flatten(policy, 1)

        # value head
        value = self.value_conv1(x)
        # value = self.value_norm1(value)
        value = F.relu(value)
        value = torch.flatten(value, 1)
        value = self.value_fc1(value)
        value = F.relu(value)
        value = self.value_fc2(value)
        return policy, value
