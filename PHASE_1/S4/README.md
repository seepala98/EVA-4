# Code Drill Down
### all model have been trained for 20 epochs to verify if the accuracy is maintained.

## [Step_1](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_1.ipynb)

#### Target : get the model with better parameters than 6.3M 

#### Result :
```
Params : 194k. 
Train Accuracy : 99.39 (18th epoch). 
Test Accuracy : 99.04 (19th epoch)   
```
#### Analysis : 
Convert the model that has parameters from 6.3M to 194k but the accuracy will be reduced as the model lost a lot of parameters and the convolution layers are not written properly need to design the model and increase the capacity of the model. 

## [Step_2](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_2.ipynb)

#### Target :   
Reduce the parameters further more in under 10K. This can be achieved bu tweaking the convolution Network, add BatchNorm , Relu , Gap .   

#### Result :
```
Params : 9606. 
Train Accuracy : 99.69 (17th epoch). 
Test Accuracy : 99.33 (17th epoch)   
```
#### Analysis : 
Model is still overfitting and not reaching the accurace of 99.4 we need so we need to apply regularization like drop out to reduce over fitting .

## [Step_3](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_3.ipynb)

#### Target : 
Regularization applied as Dropout() but not on every layer.And the drop shouldnt be too high that the model cant learn or too less to be of no use applying .

#### Result :
```
Params : 9606
Train Accuracy : 99.44 (18,19th epoch)
Test Accuracy : 99.45 (13,16,17th epoch) 
```
#### Analysis : 
No over fitting as the test and train accuracies are close. So the loss is getting lower so this helps in getting the desired 99.4% in lesser epoch.

## [Step_4](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_4.ipynb)

#### Target : 
Add image augumentation as the image angles varies around 5-7 degrees so augumentation is applied on the train data. to train the model better and apply other optimizers (SGD ,adam)

#### Result :
```
Params : 9606
Train Accuracy : 99.24 (18th epoch)
Test Accuracy : 99.43 (14th epoch) , above 99.4 (8,14,16,17,18,19th epoch) 
```
#### Analysis : 
As the image Augumentation helped in training the model for slight transformation to the data like change of angle. But now we have consistence in getting 99.4 % accuracy. Tried with adam optimizer but the results were not satisfying (https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_4_adam.ipynb) 

## [Step_5](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S4/step_5.ipynb)

#### Target : 
Implement LR Schedulers as this helps in model to move towards local minima that inturn mean lesser loss. But choosing a LR schedular is hard tried with StepLR and ExponentialLR.

#### Result :
```
Params : 9606
Train Accuracy : 99.17 (10th epoch)
Test Accuracy : 99.42(15th epoch) , 99.45 (17th epoch) and consistant 99.4% accuracy on test data 
```
#### Analysis : 
Due to the use of Schedulers, the StepLR will increment the learning rate on regular intervals. This seems to have helped to achieve the desired results of > 99.4% on test Accuracy under 10k params and under 15 epochs.
