from albumentations import Compose, Normalize, HorizontalFlip, Cutout ,Rotate ,PadIfNeeded ,RandomCrop
#from imgaug.augmenters.arithmetic import CoarseDropout
from albumentations.pytorch import ToTensor
import numpy as np

class TrainAlbumentation():
  def __init__(self):
    self.train_transform = Compose([
      HorizontalFlip(),
      Rotate((-10.0, 10.0)),
      Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225],
      ),
      #CoarseDropout(p=(0.02, 0.1), size_px=None, size_percent=None, per_channel=False, min_size=3, seed=None, name=None, random_state='deprecated', deterministic='deprecated')
      #CoarseDropout(max_holes = 1, max_height = 6, max_width = 6, fill_value = [0.485, 0.456, 0.406], p = 0.5),
      PadIfNeeded(min_height=40, min_width=40, border_mode=4, always_apply=False,value=0, p=1.0),
      RandomCrop(height=32, width=32, always_apply=True, p=1.0),
      Cutout(num_holes=1, max_h_size=6, max_w_size=6, p=0.5),
      ToTensor(),
    ])

  def __call__(self, img):
    img = np.array(img)
    img = self.train_transform(image = img)['image']
    return img
