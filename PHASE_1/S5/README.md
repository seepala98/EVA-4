# S6 - Regularization 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seepala98/EVA-4/blob/master/PHASE_1/S5/Assinment_6.ipynb)

The goal of this assignment is to apply L1 and L2 regularization on the final model from the [previous](../S4/) session and plot the changes in validation loss and accuracy obtained during model training in the following scenarios:

1. Without L1 and L2 regularization
2. With L1 regularization
3. With L2 regularization
4. With L1 and L2 regularization

After model training, display 25 misclassified images for L1 and L2 models.

### Parameters and Hyperparameters

- Kernel Size: 3x3
- Loss Function: Negative Log Likelihood
- Optimizer: SGD
- Dropout Rate: 0.05
- Batch Size: 64
- Learning Rate: 0.01
- **L1 Factor:** 0.005
- **L2 Factor:** 0.005

## Results

### Change in Validation Loss and Accuracy

<img src="images/LOSS_GRAPH.png" width="600px">
<img src="images/ACCURACY_GRAPH.png" width="600px">

## Misclassified Images

### Without L1 and L2 Regularization

![plain](images/INCORRECT_WITHOUT_L1_L2.png)

### With L1 Regularization

![plain](images/INCORRECT_WITH_L1.png)

### With L2 Regularization

![plain](images/INCORRECT_WITH_L2.png)

### With L1 AND L2 Regularization

![plain](images/INCORRECT_WITH_L1_AND_L2.png)
