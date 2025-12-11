import torch
import torch.nn as nn

class_weights = torch.tensor([1., 2.])
criterion = nn.CrossEntropyLoss(weight=class_weights)