## MNIST dataset to achieve 99.4% accuracy in under 20k parameters 

### Best accuracy was achieved at epoch : 20 

### Best Accuracy:

`epoch = 20 loss=0.0003819465637207031 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 30.92it/s]
Test set: Average loss: 0.0211, Accuracy: 9947/10000 (99.4700%)`

### Total Parameters :  18,306 

```
Requirement already satisfied: torchsummary in /usr/local/lib/python3.6/dist-packages (1.5.1)
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 28, 28]              72
       BatchNorm2d-2            [-1, 8, 28, 28]              16
            Conv2d-3           [-1, 16, 28, 28]           1,152
       BatchNorm2d-4           [-1, 16, 28, 28]              32
         MaxPool2d-5           [-1, 16, 14, 14]               0
            Conv2d-6           [-1, 32, 14, 14]           4,608
       BatchNorm2d-7           [-1, 32, 14, 14]              64
            Conv2d-8           [-1, 32, 12, 12]           9,248
       BatchNorm2d-9           [-1, 32, 12, 12]              64
        MaxPool2d-10             [-1, 32, 6, 6]               0
           Conv2d-11             [-1, 16, 6, 6]             512
      BatchNorm2d-12             [-1, 16, 6, 6]              32
           Conv2d-13             [-1, 16, 4, 4]           2,304
      BatchNorm2d-14             [-1, 16, 4, 4]              32
AdaptiveAvgPool2d-15             [-1, 16, 1, 1]               0
           Conv2d-16             [-1, 10, 1, 1]             170
================================================================
Total params: 18,306
Trainable params: 18,306
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.50
Params size (MB): 0.07
Estimated Total Size (MB): 0.57
----------------------------------------------------------------
```

