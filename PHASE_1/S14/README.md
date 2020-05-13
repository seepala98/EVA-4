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

FG_BG zip : https://drive.google.com/open?id=12ZEX7cPURtBodYUkpY5hl-iKrbBEYlBW

FG_BG_MASK : https://drive.google.com/open?id=1-9dpdC9Cq09PiMZZG-zanYQuxV2QiXvt

DEPTH_MAP : (divided to 5 zip files each with 80k images)

depth_1 : https://drive.google.com/open?id=1ltTX55fRiKIYulUTsXTmYXGh9qPll78U

depth_2 : https://drive.google.com/open?id=1_3PDGuTzSJf6Pj0AlW7rk8WSC6ZuR4AM

depth_3 : https://drive.google.com/open?id=1-3gCYT0XfjK3jcBRXnhuZhWN9wjwNQhI

depth_4 : https://drive.google.com/open?id=19zh02qFNGJl4AfO6K_QFP3sPbHdgt2OC

depth_5 : https://drive.google.com/open?id=1-DYPPJVmZSls1xXnRjJx7xqgQ2rPbta-



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

- Mean: `['0.445187151432037', '0.453919172286987', '0.442775547504425']`
- Std:  `['0.209829792380333', '0.204434618353844', '0.218459352850914']`

2. FG_BG Images

- Mean: `['0.458231598138809', '0.458402276039124', '0.454385221004486']`
- Std:  `['0.216196656227112', '0.213248178362846', '0.224730432033539']`

3. FG_BG_MASK Images

- Mean: `['0.246712774038315', '0.246712774038315', '0.246712774038315']`
- Std: `['0.419586002826691', '0.419586002826691', '0.419586002826691']`

4. DEPTH_FG_BG

- Mean: `['0.180530488491058', '0.180530488491058', '0.180530488491058']`
- Std: `['0.051506847143173', '0.051506847143173', '0.051506847143173']`

## Dataset Visualization

Github Link: [https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_04_DataVisualization.ipynb](https://github.com/seepala98/EVA-4/blob/master/PHASE_1/S14/S15A_04_DataVisualization.ipynb)

Colab Link: https://colab.research.google.com/drive/1_eWpgpKEnJGTtQPn5t_2VtCPNYQDhxNN

# How the data set has been created : 

FG : Download 100 images with transparent background from the internet and clean the data and by verifying if all the images are transparent if not make them transparent by using power point .

BG : Downloaded 100 images of parking spaces and empty roads from the internet. 

FG_BG : take the images of fg and bg and scale them to 250,250 by using the changeImageSize code
```
def changeImageSize(maxWidth,maxHeight,image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage
```
Then pass the image to the changeImageSize function , use the PIL.FLIP_LEFT_RIGHT to get the left right of the image 

Rescale the images:
```
try:
        bg = Image.open(f'{path}bg/park{str(i)}.jpg')
        bg = changeImageSize(250, 250, bg)
        print(f'{path}bg/park{str(i)}.jpg')
    except :
        print("park not found")
        continue
```

Left_right the fg:
```
flipfg = fg1.transpose(PIL.Image.FLIP_LEFT_RIGHT) 
flipmask = m1.transpose(PIL.Image.FLIP_LEFT_RIGHT)
```

And to get the fg placed at 20 random location on bg used random.randint(1,80).

Depth model : 

we need to create the depth map, by running the DenseDepth Model on our fg_bg images, this was done by taking batches of 1000.
