# CIFAR-10

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seepala98/EVA-4/blob/master/PHASE_1/S7/CIFAR_10_S7.ipynb)

## Best Accuracy on train data :
```
Epoch 45:
Loss=0.18 Batch ID=390 Accuracy=92.97: 100%|██████████| 391/391 [00:11<00:00, 33.27it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0047, Accuracy: 8331/10000 (83.31%)
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
Accuracy of plane : 86 %
Accuracy of   car : 91 %
Accuracy of  bird : 72 %
Accuracy of   cat : 71 %
Accuracy of  deer : 82 %
Accuracy of   dog : 71 %
Accuracy of  frog : 90 %
Accuracy of horse : 80 %
Accuracy of  ship : 91 %
Accuracy of truck : 89 %
```