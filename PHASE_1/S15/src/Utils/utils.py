import torchvision
import matplotlib.pyplot as plt

from zipfile import ZipFile

def extract_zip(filename):
  try:
    with ZipFile(filename, 'r') as zip:
      print("Extracting zip file contents now")
      zip.extractall()
      print("Done!")
  except:
    print("This file doenst Exist")
    
def show(tensors, figsize= (10,10), *args, **kwargs):
  try:
    tensors = tensors.detach().cpu()
  except:
    pass
  grid_tensor = torchvision.utils.make_grid(tensors, *args, **kwargs)  
	grid_image  = grid_tensor.permute(1, 2, 0)
	plt.figure(figsize = figsize)
	plt.imshow(grid_image)
	plt.xticks([])  
	plt.yticks([])
	plt.show()
