# RCNN and Depth Assignment

You must have 100 background, 100x2 (including flip), and you randomly place the foreground on the background 20 times, you have in total 100x200x20 images.

In total you MUST have:

1.  400k fg_bg images
2.  400k depth images
3.  400k mask images
4.  generated from:
    1.  100 backgrounds
    2.  100 foregrounds, plus their flips
    3.  20 random placement on each background.
5.  Now add a readme file on GitHub for Project 15A:
    1.  Create this dataset and share a link to GDrive (publicly available to anyone) in this readme file.
    2.  Add your dataset statistics:
        1.  Kinds of images (fg, bg, fg_bg, masks, depth)
        2.  Total images of each kind
        3.  The total size of the dataset
        4.  Mean/STD values for your fg_bg, masks and depth images
    3.  Show your dataset the way I have shown above in this readme
    4.  Explain how you created your dataset
        1.  how were fg created with transparency
        2.  how were masks created for fgs
        3.  how did you overlay the fg over bg and created 20 variants
        4.  how did you create your depth images?
6.  Add the notebook file to your repo, one which you used to create this dataset
7.  Add the notebook file to your repo, one which you used to calculate statistics for this dataset

Things to remember while creating this dataset:

1.  stick to square images to make your life easy.
2.  We would use these images in a network which would take an fg_bg image AND bg image, and predict your MASK and Depth image. So the input to the network is, say, 224x224xM and 224x224xN, and the output is 224x224xO and 224x224xP.
3.  pick the resolution of your choice between 150 and 250 for ALL the images

# Solution

## Dataset Google Drive links:

FG zip : https://drive.google.com/open?id=1fRFlZgKb8FCrOsTbKlDOad4oOJB3jong

BG zip : https://drive.google.com/open?id=1n3FLLwUfKAA88HQL0fe4kE6-mHnE0HaW

FG_BG zip : https://drive.google.com/open?id=1kP1ItxxybZZP-djFu4Jgqsyc3KgTmR_J

FG_BG_MASK : https://drive.google.com/open?id=1-9dpdC9Cq09PiMZZG-zanYQuxV2QiXvt

DEPTH_MAP : https://drive.google.com/open?id=1-CL8A38YykVT7HAPqfuYBZSJHXnHtEOL


### BG Images

![enter image description here](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/images/bg.png)

### FG Images

![enter image description here](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/images/fg.png)

### FG_BG Images

![enter image description here](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/images/fg_bg.png)

### FG_BG_MASK Images

![enter image description here](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/images/fg_bg_mask.png)

### Depth_FG_BG Images

![enter image description here](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/images/depth_images.png)

## Dataset Creation

Github Link: [https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_01_DataCreation.ipynb](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_01_DataCreation.ipynb)

Colab Link: https://colab.research.google.com/drive/1Xq97nuZyU1t4-jBDHCGaHvDc646zqpV7

## Depth Map creation

github link : [https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_02_DepthMap.ipynb](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_02_DepthMap.ipynb)

Colab link: [https://colab.research.google.com/drive/1i_lmD_O0IMUhY3pLO_DnojLbjgs15GRG](https://colab.research.google.com/drive/1i_lmD_O0IMUhY3pLO_DnojLbjgs15GRG)

## Mean and Standard Deviation

Github Link: [https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_03_stats.ipynb](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_03_stats.ipynb)

Colab Link: https://colab.research.google.com/drive/1ygfJO2BfXNMfsiLlWLAM_poq-vXIwHAk

### Dataset Stats:

1. BG Images

- Mean:`['0.445187121629715', '0.453919261693954', '0.442775547504425']`
- Std: `['0.209829762578011', '0.204434663057327', '0.218459382653236']`

2. FG_BG Images

- Mean: `['0.430746674537659', '0.430641651153564', '0.428456991910934']`
- Std:  `['0.233161732554436', '0.229639455676079', '0.240961566567421']`

3. FG_BG_MASK Images

- Mean: `['0.246706947684288', '0.246706947684288', '0.246706947684288']`
- Std: `['0.419592112302780', '0.419592112302780', '0.419592112302780']`

4. DEPTH_FG_BG

- Mean: `['0.185273632407188', '0.185273632407188', '0.185273632407188']`
- Std: `['0.056562200188637', '0.056562200188637', '0.056562200188637']`

There has been a data corruption in the zip file of depth_fg_bg maps due to several failues the images generated are around 269273.
## Dataset Visualization

Github Link: [https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_04_DataVisualization.ipynb](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_04_DataVisualization.ipynb)

Colab Link: https://colab.research.google.com/drive/1_eWpgpKEnJGTtQPn5t_2VtCPNYQDhxNN
