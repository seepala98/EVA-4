import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np

# functions to show an image
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    fig = plt.figure(figsize=(2,2))
    plt.imshow(np.transpose(npimg, (1, 2, 0)),interpolation='none')
    plt.title(c)
    
def show_train_data(dataset, classes):

  # get some random training images

  dataiter = iter(dataset)
  images, labels = dataiter.next()
  for i in range(len(classes)):
    index = [j for j in range(1) if labels[j] == i]
    if(len(index) > 0):
      imshow(torchvision.utils.make_grid(images[index],nrow=1,padding=2,scale_each=True),classes[i])
