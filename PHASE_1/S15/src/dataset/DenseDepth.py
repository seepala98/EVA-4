from pathlib import Path
import os
from torch.utils.data import Dataset
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm
import numpy as np
from PIL import Image
import PIL
import zipfile
from zipfile import ZipFile
from zipfile import ZipFile as zip

sns.set()


class DenseDepth(Dataset):
  bg_stat = (['0.445187151432037', '0.453919172286987', '0.442775547504425'], 
               ['0.209829792380333', '0.204434618353844', '0.218459352850914'])
  fg_bg_stat = (['0.458231598138809', '0.458402276039124', '0.454385221004486'], 
                  ['0.216196656227112', '0.213248178362846', '0.224730432033539'])
  fg_bg_mask_stat = (['0.246712774038315', '0.246712774038315', '0.246712774038315'], 
                       ['0.419586002826691', '0.419586002826691', '0.419586002826691'])
  depth_fg_bg_stat = (['0.180530488491058', '0.180530488491058', '0.180530488491058'], 
                        ['0.051506847143173', '0.051506847143173', '0.051506847143173'])

  def __init__(self, root, train=True, transform=None, target_transform=None):
    self.root = Path(root) / 'data_all'
    self.root.mkdir(parents=True, exist_ok=True)
    self.transform = transform
    self.target_transform = target_transform

    # check if the dataset exists
    if os.path.isdir(self.root / 'bg') or os.path.isdir(self.root / 'fg_bg') or os.path.isdir(self.root / 'fg_bg_mask') or os.path.isdir(self.root / 'fg_bg_depth'):
      print(f'dataset folders/files already exists in {self.root}')

    # pathlib does not order them by default
    bg_paths = sorted(list(Path(self.root / 'bg').glob('*.jpg')))
    fg_bg_paths = sorted(list(Path(self.root / 'fg_bg').glob('**/*.jpg')))
    fg_bg_mask_paths = sorted(list(Path(self.root / 'fg_bg_mask').glob('**/*.jpg')))
    depth_fg_bg_paths = sorted(list(Path(self.root / 'fg_bg_depth').glob('**/*.png')))

    assert(len(bg_paths) == 100)
    assert(len(fg_bg_paths) == 400000)
    assert(len(fg_bg_mask_paths) == 400000)
    assert(len(depth_fg_bg_paths) == 400000)

    print(f'found {len(bg_paths)} bg images, {len(fg_bg_paths)} fg_bg images, {len(fg_bg_mask_paths)} fg_bg_mask images, {len(depth_fg_bg_paths)} depth_fg_bg images')

    self.input_paths = fg_bg_paths
    self.bg_paths = bg_paths
    self.target_paths_mask = fg_bg_mask_paths
    self.target_paths_depth = depth_fg_bg_paths

    def __getitem__(self, index):
      bgidx = self.input_paths[index].stem.split('_')[3]
      bgimg = Image.open(self.bg_paths[int(bgidx)])
      bgimg = bgimg.convert('RGB')
      # bgimg = np.array(bgimg)

      fg_bgimg = Image.open(self.input_paths[index])
      fg_bgimg = fg_bgimg.convert('RGB')
      # fg_bgimg = np.array(fg_bgimg)

      target_mask = self.target_paths_mask[index]
      target_depth = self.target_paths_depth[index]

      mask_fg_bgimg = Image.open(target_mask)
      mask_fg_bgimg.convert('L')
      mask_arr = np.array(mask_fg_bgimg)
      mask_arr[mask_arr >= 150] = 255
      mask_arr[mask_arr < 150] = 0
      mask_fg_bgimg = Image.fromarray(mask_arr)
      # mask_fg_bgimg.convert('L')
      
      depth_fg_bgimg = Image.open(target_depth)
      depth_fg_bgimg.convert('L')

      if self.transform is not None:
        bgimg = self.transform(bgimg)
        fg_bgimg = self.transform(fg_bgimg)
      
      if self.target_transform is not None:
        mask_fg_bgimg = self.target_transform(mask_fg_bgimg)
        depth_fg_bgimg = self.target_transform(depth_fg_bgimg)
    return {'bg': bgimg, 'fg_bg': fg_bgimg, 'fg_bg_mask': mask_fg_bgimg, 'depth_fg_bg': depth_fg_bgimg}

  def __len__(self):
    return len(self.input_paths)

  @staticmethod
  def plot_sample(sample):
    '''
    Plots a given sample of the dataset
    '''
    bg, fg_bg, fg_bg_mask, depth_fg_bg = sample['bg'].permute(1, 2, 0).numpy(), sample['fg_bg'].permute(
      1, 2, 0).numpy(), sample['fg_bg_mask'][0].numpy(), sample['depth_fg_bg'][0].numpy()
    fig, ax = plt.subplots(2, 2, figsize=(4, 4), sharex=True, sharey=True)

    ax[0, 0].imshow(bg)
    ax[0, 0].axis('off')
    
    ax[0, 1].imshow(fg_bg)
    ax[0, 1].axis('off')

    ax[1, 0].imshow(fg_bg_mask)
    ax[1, 0].axis('off')
    
    ax[1, 1].imshow(depth_fg_bg)
    ax[1, 1].axis('off')
    
    fig.tight_layout()
    plt.show()
 
  @staticmethod
  def plot4_batch(batch):
    '''
    Plots 4 images for batch
    '''
    fig, ax = plt.subplots(4, 4, figsize=(6, 6), sharex=True, sharey=True)
    
    # set the title
    for axs, col in zip(ax[0], ['BG', 'FG_BG', 'FG_BG_MASK', 'DEPTH_FG_BG']):
      axs.set_title(col)
      
    # plot the first 4 samples from the batch
    for i in range(4):
      bg, fg_bg, fg_bg_mask, depth_fg_bg = batch['bg'][i].permute(1, 2, 0).numpy(), batch['fg_bg'][i].permute(
        1, 2, 0).numpy(), batch['fg_bg_mask'][i][0].numpy(), batch['depth_fg_bg'][i][0].numpy()
      
      ax[i, 0].imshow(bg)
      ax[i, 0].axis('off')
      
      ax[i, 1].imshow(fg_bg)
      ax[i, 1].axis('off')

      ax[i, 2].imshow(fg_bg_mask)
      ax[i, 2].axis('off')

      ax[i, 3].imshow(depth_fg_bg)
      ax[i, 3].axis('off')

      fig.tight_layout()
      
      plt.show()
