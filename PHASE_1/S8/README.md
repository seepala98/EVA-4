# CIFAR10 WITH RESNET18 Architecture

## Observation :
Best Test Accuracy : 90.41 % under 30 epochs and achieved 85% accuracy in under 10 epochs consistantly

## Logs : 
```
  0%|          | 0/391 [00:00<?, ?it/s]
Epoch 1:
Loss=1.16 Batch ID=390 Accuracy=43.57: 100%|██████████| 391/391 [00:53<00:00,  7.32it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0099, Accuracy: 5537/10000 (55.37%)

Epoch 2:
Loss=1.25 Batch ID=390 Accuracy=63.44: 100%|██████████| 391/391 [00:54<00:00,  7.21it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0100, Accuracy: 6042/10000 (60.42%)

Epoch 3:
Loss=0.58 Batch ID=390 Accuracy=72.08: 100%|██████████| 391/391 [00:55<00:00,  7.08it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0069, Accuracy: 7049/10000 (70.49%)

Epoch 4:
Loss=0.57 Batch ID=390 Accuracy=77.34: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0052, Accuracy: 7714/10000 (77.14%)

Epoch 5:
Loss=0.45 Batch ID=390 Accuracy=80.22: 100%|██████████| 391/391 [00:56<00:00,  6.93it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0047, Accuracy: 8060/10000 (80.60%)

Epoch 6:
Loss=0.42 Batch ID=390 Accuracy=83.15: 100%|██████████| 391/391 [00:56<00:00,  6.91it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0042, Accuracy: 8211/10000 (82.11%)

Epoch 7:
Loss=0.48 Batch ID=390 Accuracy=84.40: 100%|██████████| 391/391 [00:56<00:00,  6.95it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0045, Accuracy: 8197/10000 (81.97%)

Epoch 8:
Loss=0.53 Batch ID=390 Accuracy=86.23: 100%|██████████| 391/391 [00:56<00:00,  6.92it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0041, Accuracy: 8267/10000 (82.67%)

Epoch 9:
Loss=0.38 Batch ID=390 Accuracy=87.03: 100%|██████████| 391/391 [00:56<00:00,  6.93it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0036, Accuracy: 8548/10000 (85.48%)

Epoch 10:
Loss=0.33 Batch ID=390 Accuracy=87.90: 100%|██████████| 391/391 [00:56<00:00,  6.96it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0032, Accuracy: 8634/10000 (86.34%)

Epoch 11:
Loss=0.23 Batch ID=390 Accuracy=89.20: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0038, Accuracy: 8522/10000 (85.22%)

Epoch 12:
Loss=0.31 Batch ID=390 Accuracy=89.94: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0031, Accuracy: 8700/10000 (87.00%)

Epoch 13:
Loss=0.31 Batch ID=390 Accuracy=90.56: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0031, Accuracy: 8746/10000 (87.46%)

Epoch 14:
Loss=0.18 Batch ID=390 Accuracy=90.90: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8777/10000 (87.77%)

Epoch 15:
Loss=0.20 Batch ID=390 Accuracy=91.61: 100%|██████████| 391/391 [00:56<00:00,  6.98it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0036, Accuracy: 8654/10000 (86.54%)

Epoch 16:
Loss=0.12 Batch ID=390 Accuracy=92.23: 100%|██████████| 391/391 [00:55<00:00,  7.02it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0032, Accuracy: 8731/10000 (87.31%)

Epoch 17:
Loss=0.13 Batch ID=390 Accuracy=92.86: 100%|██████████| 391/391 [00:55<00:00,  7.01it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8849/10000 (88.49%)

Epoch 18:
Loss=0.24 Batch ID=390 Accuracy=93.13: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0033, Accuracy: 8798/10000 (87.98%)

Epoch 19:
Loss=0.18 Batch ID=390 Accuracy=93.69: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8916/10000 (89.16%)

Epoch 20:
Loss=0.18 Batch ID=390 Accuracy=93.96: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 8883/10000 (88.83%)

Epoch 21:
Loss=0.14 Batch ID=390 Accuracy=94.25: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0031, Accuracy: 8864/10000 (88.64%)

Epoch 22:
Loss=0.13 Batch ID=390 Accuracy=94.71: 100%|██████████| 391/391 [00:55<00:00,  7.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8931/10000 (89.31%)

Epoch 23:
Loss=0.20 Batch ID=390 Accuracy=94.94: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8952/10000 (89.52%)

Epoch 24:
Loss=0.14 Batch ID=390 Accuracy=95.23: 100%|██████████| 391/391 [00:56<00:00,  6.98it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 8950/10000 (89.50%)

Epoch 25:
Loss=0.12 Batch ID=390 Accuracy=95.67: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0031, Accuracy: 8933/10000 (89.33%)

Epoch 26:
Loss=0.06 Batch ID=390 Accuracy=95.78: 100%|██████████| 391/391 [00:55<00:00,  6.99it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 9040/10000 (90.40%)

Epoch 27:
Loss=0.16 Batch ID=390 Accuracy=96.05: 100%|██████████| 391/391 [00:56<00:00,  6.98it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0031, Accuracy: 8935/10000 (89.35%)

Epoch 28:
Loss=0.09 Batch ID=390 Accuracy=96.20: 100%|██████████| 391/391 [00:55<00:00,  7.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 9041/10000 (90.41%)

Epoch 29:
Loss=0.09 Batch ID=390 Accuracy=96.28: 100%|██████████| 391/391 [00:55<00:00,  7.00it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 9030/10000 (90.30%)

Epoch 30:
Loss=0.14 Batch ID=390 Accuracy=96.66: 100%|██████████| 391/391 [00:55<00:00,  7.03it/s]
Validation set: Average loss: 0.0033, Accuracy: 8970/10000 (89.70%)
```
