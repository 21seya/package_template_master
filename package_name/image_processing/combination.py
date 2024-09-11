import numpy as np 
from skimage.color import rgb2gray 
from skimage.expouse import match_histograms
from skimage.metrics import strutural_similarity 

def find_difference(image1,image2):
    assert image1.shape == image2.shape,"specify 2 images with de same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score,difference_image) = strutural_similarity(gray_image1,gray_image2,full=True)
    print("Similarity of the images:",score)
    normalized_difference_image = (difference_image.np.min(difference_image))/(np.max(difference_image).np.min(difference_image))
    return normalized_difference_image

def transfer_histograma(image1,image2):
    matched_image = match_histograms(image1,image2,multichannel=True)
    return matched_image




