import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import os


path = "C:/Users/User/Documents/EBTECH/dataset/cannon/add" 
list_img = os.listdir(path)
print (list_img)

ia.seed(1)
j=1
for pic in list_img:
    img = imageio.imread(os.path.join(str(path) ,str(pic))) #read you image
    images = np.array(
        [img for _ in range(5)], dtype=np.uint8)  # 32 means creat 32 enhanced images using following methods.

    seq = iaa.Sequential([
        iaa.Fliplr(0.5), # horizontal flips
        iaa.Crop(percent=(0, 0.1)), # random crops
        # Small gaussian blur with random sigma between 0 and 0.5.
        # But we only blur about 50% of all images.
        iaa.Sometimes(
            0.5,
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        # Strengthen or weaken the contrast in each image.
        iaa.LinearContrast((0.75, 1.5)),
        # Add gaussian noise.
        # For 50% of all images, we sample the noise once per pixel.
        # For the other 50% of all images, we sample the noise per pixel AND
        # channel. This can change the color (not only brightness) of the
        # pixels.
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        # Make some images brighter and some darker.
        # In 20% of all cases, we sample the multiplier once per channel,
        # which can end up changing the color of the images.
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        # Apply affine transformations to each image.
        # Scale/zoom them, translate/move them, rotate them and shear them.
        
    ], random_order=True) # apply augmenters in random order

    images_aug = seq.augment_images(images)

    for i in range(5):
        imageio.imwrite('C:/Users/User/Documents/EBTECH/dataset/cannon/train2/Pic_'+str(j)+"_"+str(i)+'.jpg', images_aug[i])  #write all changed images
    j=j+1
        
        
        
"""
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import os


path = "C:/Users/User/Documents/EBTECH/dataset/cannon/Pic"
list_img = os.listdir(path)
print (list_img)

ia.seed(1)
j=1
for pic in list_img:
    img = imageio.imread(os.path.join(str(path) ,str(pic))) #read you image
    images = np.array(
        [img for _ in range(12)], dtype=np.uint8)  # 32 means creat 32 enhanced images using following methods.

    seq = iaa.Sequential([
        iaa.Fliplr(0.5), # horizontal flips
        iaa.Crop(percent=(0, 0.1)), # random crops
        # Small gaussian blur with random sigma between 0 and 0.5.
        # But we only blur about 50% of all images.
        iaa.Sometimes(
            0.5,
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        # Strengthen or weaken the contrast in each image.
        iaa.LinearContrast((0.75, 1.5)),
        # Add gaussian noise.
        # For 50% of all images, we sample the noise once per pixel.
        # For the other 50% of all images, we sample the noise per pixel AND
        # channel. This can change the color (not only brightness) of the
        # pixels.
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        # Make some images brighter and some darker.
        # In 20% of all cases, we sample the multiplier once per channel,
        # which can end up changing the color of the images.
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        # Apply affine transformations to each image.
        # Scale/zoom them, translate/move them, rotate them and shear them.
        iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
            rotate=(-25, 25),
            shear=(-8, 8)
        )
    ], random_order=True) # apply augmenters in random order

    images_aug = seq.augment_images(images)

    for i in range(12):
        imageio.imwrite('C:/Users/User/Documents/EBTECH/dataset/cannon/train/Pic_'+str(j)+"_"+str(i)+'.jpg', images_aug[i])  #write all changed images
    j=j+1
        

"""