# CIFAR-10

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seepala98/EVA-4/blob/master/PHASE_1/S7/FINAL_CIFAR_10_S7.ipynb)

## Best Accuracy on train data :
```
Epoch 43:
Loss=0.22 Batch ID=390 Accuracy=92.71: 100%|██████████| 391/391 [00:15<00:00, 25.87it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0044, Accuracy: 8376/10000 (83.76%)
```

## Layers : 

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 32, 32]             896
              ReLU-2           [-1, 32, 32, 32]               0
       BatchNorm2d-3           [-1, 32, 32, 32]              64
           Dropout-4           [-1, 32, 32, 32]               0
            Conv2d-5           [-1, 64, 32, 32]          18,496
              ReLU-6           [-1, 64, 32, 32]               0
       BatchNorm2d-7           [-1, 64, 32, 32]             128
           Dropout-8           [-1, 64, 32, 32]               0
         MaxPool2d-9           [-1, 64, 16, 16]               0
           Conv2d-10           [-1, 32, 16, 16]           2,080
           Conv2d-11           [-1, 32, 16, 16]           9,248
             ReLU-12           [-1, 32, 16, 16]               0
      BatchNorm2d-13           [-1, 32, 16, 16]              64
          Dropout-14           [-1, 32, 16, 16]               0
           Conv2d-15           [-1, 64, 16, 16]          18,496
             ReLU-16           [-1, 64, 16, 16]               0
      BatchNorm2d-17           [-1, 64, 16, 16]             128
          Dropout-18           [-1, 64, 16, 16]               0
        MaxPool2d-19             [-1, 64, 8, 8]               0
           Conv2d-20             [-1, 32, 8, 8]           2,080
           Conv2d-21             [-1, 32, 8, 8]           9,248
             ReLU-22             [-1, 32, 8, 8]               0
      BatchNorm2d-23             [-1, 32, 8, 8]              64
          Dropout-24             [-1, 32, 8, 8]               0
           Conv2d-25             [-1, 32, 8, 8]             320
           Conv2d-26             [-1, 64, 8, 8]           2,112
             ReLU-27             [-1, 64, 8, 8]               0
      BatchNorm2d-28             [-1, 64, 8, 8]             128
          Dropout-29             [-1, 64, 8, 8]               0
        MaxPool2d-30             [-1, 64, 4, 4]               0
           Conv2d-31             [-1, 32, 4, 4]           2,080
           Conv2d-32             [-1, 32, 4, 4]           9,248
             ReLU-33             [-1, 32, 4, 4]               0
      BatchNorm2d-34             [-1, 32, 4, 4]              64
          Dropout-35             [-1, 32, 4, 4]               0
           Conv2d-36             [-1, 64, 2, 2]          18,496
             ReLU-37             [-1, 64, 2, 2]               0
      BatchNorm2d-38             [-1, 64, 2, 2]             128
          Dropout-39             [-1, 64, 2, 2]               0
AdaptiveAvgPool2d-40             [-1, 64, 1, 1]               0
           Linear-41                   [-1, 10]             650
================================================================
Total params: 94,218
Trainable params: 94,218
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 4.22
Params size (MB): 0.36
Estimated Total Size (MB): 4.59
----------------------------------------------------------------
```

# Val Accuracys for each class : 
```
Accuracy of plane : 85 %
Accuracy of   car : 91 %
Accuracy of  bird : 73 %
Accuracy of   cat : 74 %
Accuracy of  deer : 84 %
Accuracy of   dog : 72 %
Accuracy of  frog : 88 %
Accuracy of horse : 86 %
Accuracy of  ship : 92 %
Accuracy of truck : 86 %
```
# Loss Graph :
![Image description](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S7/loss_cifar_10.png)

# Accuracy Graph :
![Image description](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S7/accuracy_cifar10.png)

## Tried implementing in a hierarchial structure but for some reason the accuracies are taking more epochs than usual to achive the 80% 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seepala98/EVA-4/blob/master/PHASE_1/S7/base.ipynb)
