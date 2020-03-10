# CIFAR10 WITH RESNET18 Architecture

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seepala98/EVA-4/blob/master/PHASE_1/S8/CIFAR_RESNET18.ipynb)

## Observation :
Best Test Accuracy : 91.02 % under 30 epochs and achieved 85% accuracy in under 10 epochs consistantly

## Logs : 
```
  0%|          | 0/391 [00:00<?, ?it/s]Epoch 1:
Loss=1.22 Batch ID=390 Accuracy=43.11: 100%|██████████| 391/391 [00:29<00:00, 14.48it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0106, Accuracy: 5333/10000 (53.33%)

Epoch 2:
Loss=1.22 Batch ID=390 Accuracy=63.20: 100%|██████████| 391/391 [00:29<00:00, 14.55it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0097, Accuracy: 6269/10000 (62.69%)

Epoch 3:
Loss=0.58 Batch ID=390 Accuracy=72.70: 100%|██████████| 391/391 [00:28<00:00, 14.60it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0077, Accuracy: 6850/10000 (68.50%)

Epoch 4:
Loss=0.61 Batch ID=390 Accuracy=77.76: 100%|██████████| 391/391 [00:29<00:00, 13.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0051, Accuracy: 7784/10000 (77.84%)

Epoch 5:
Loss=0.55 Batch ID=390 Accuracy=80.69: 100%|██████████| 391/391 [00:29<00:00, 14.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0044, Accuracy: 8125/10000 (81.25%)

Epoch 6:
Loss=0.41 Batch ID=390 Accuracy=83.07: 100%|██████████| 391/391 [00:29<00:00, 14.59it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0042, Accuracy: 8206/10000 (82.06%)

Epoch 7:
Loss=0.49 Batch ID=390 Accuracy=84.57: 100%|██████████| 391/391 [00:28<00:00, 14.59it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0038, Accuracy: 8414/10000 (84.14%)

Epoch 8:
Loss=0.70 Batch ID=390 Accuracy=86.28: 100%|██████████| 391/391 [00:29<00:00, 13.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0047, Accuracy: 8184/10000 (81.84%)

Epoch 9:
Loss=0.41 Batch ID=390 Accuracy=86.83: 100%|██████████| 391/391 [00:28<00:00, 14.57it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0037, Accuracy: 8519/10000 (85.19%)

Epoch 10:
Loss=0.34 Batch ID=390 Accuracy=88.27: 100%|██████████| 391/391 [00:29<00:00, 14.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0040, Accuracy: 8384/10000 (83.84%)

Epoch 11:
Loss=0.25 Batch ID=390 Accuracy=89.03: 100%|██████████| 391/391 [00:28<00:00, 14.48it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0041, Accuracy: 8387/10000 (83.87%)

Epoch 12:
Loss=0.31 Batch ID=390 Accuracy=89.84: 100%|██████████| 391/391 [00:29<00:00, 14.64it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8770/10000 (87.70%)

Epoch 13:
Loss=0.29 Batch ID=390 Accuracy=90.60: 100%|██████████| 391/391 [00:29<00:00, 13.45it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8760/10000 (87.60%)

Epoch 14:
Loss=0.15 Batch ID=390 Accuracy=91.01: 100%|██████████| 391/391 [00:28<00:00, 14.70it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8754/10000 (87.54%)

Epoch 15:
Loss=0.15 Batch ID=390 Accuracy=91.69: 100%|██████████| 391/391 [00:29<00:00, 14.69it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0033, Accuracy: 8744/10000 (87.44%)

Epoch 16:
Loss=0.11 Batch ID=390 Accuracy=91.96: 100%|██████████| 391/391 [00:29<00:00, 13.30it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0032, Accuracy: 8794/10000 (87.94%)

Epoch 17:
Loss=0.13 Batch ID=390 Accuracy=92.70: 100%|██████████| 391/391 [00:29<00:00, 14.66it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 8883/10000 (88.83%)

Epoch 18:
Loss=0.20 Batch ID=390 Accuracy=93.10: 100%|██████████| 391/391 [00:28<00:00, 14.62it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0034, Accuracy: 8769/10000 (87.69%)

Epoch 19:
Loss=0.15 Batch ID=390 Accuracy=93.67: 100%|██████████| 391/391 [00:29<00:00, 14.56it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8923/10000 (89.23%)

Epoch 20:
Loss=0.19 Batch ID=390 Accuracy=93.79: 100%|██████████| 391/391 [00:29<00:00, 14.59it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8894/10000 (88.94%)

Epoch 21:
Loss=0.11 Batch ID=390 Accuracy=94.28: 100%|██████████| 391/391 [00:29<00:00, 13.38it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0032, Accuracy: 8850/10000 (88.50%)

Epoch 22:
Loss=0.11 Batch ID=390 Accuracy=94.67: 100%|██████████| 391/391 [00:29<00:00, 14.36it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8939/10000 (89.39%)

Epoch 23:
Loss=0.28 Batch ID=390 Accuracy=94.88: 100%|██████████| 391/391 [00:29<00:00, 14.56it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 8970/10000 (89.70%)

Epoch 24:
Loss=0.17 Batch ID=390 Accuracy=95.08: 100%|██████████| 391/391 [00:29<00:00, 14.55it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8952/10000 (89.52%)

Epoch 25:
Loss=0.11 Batch ID=390 Accuracy=95.45: 100%|██████████| 391/391 [00:28<00:00, 14.70it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8965/10000 (89.65%)

Epoch 26:
Loss=0.09 Batch ID=390 Accuracy=95.68: 100%|██████████| 391/391 [00:28<00:00, 14.50it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 9014/10000 (90.14%)

Epoch 27:
Loss=0.07 Batch ID=390 Accuracy=95.98: 100%|██████████| 391/391 [00:29<00:00, 13.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0029, Accuracy: 8971/10000 (89.71%)

Epoch 28:
Loss=0.15 Batch ID=390 Accuracy=96.17: 100%|██████████| 391/391 [00:28<00:00, 13.59it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0030, Accuracy: 8980/10000 (89.80%)

Epoch 29:
Loss=0.04 Batch ID=390 Accuracy=96.33: 100%|██████████| 391/391 [00:29<00:00, 14.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Validation set: Average loss: 0.0028, Accuracy: 9084/10000 (90.84%)

Epoch 30:
Loss=0.13 Batch ID=390 Accuracy=96.67: 100%|██████████| 391/391 [00:29<00:00, 14.71it/s]

Validation set: Average loss: 0.0027, Accuracy: 9102/10000 (91.02%)
```
