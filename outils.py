import cv2
import numpy as np


# Contrast enhancing
def contrast_enhancement(image):
    image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
    image_contrast = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)
    return image_contrast

# Image blurring
def blurring_image(image):
    blur_filter = np.ones((3, 3), np.float32)/9.0
    image_blur = cv2.filter2D(image, -1, blur_filter)
    return image_blur

# Image thresholding
def image_thresholding(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
    return thresholded_image

# Image sharpening
def image_sharpening(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    image_sharpened = cv2.filter2D(image, -1, kernel)
    return image_sharpened

# Showing results
# cv2.imshow('Color input image', image)
# cv2.imshow("histogram equalized", image_contrast)
# cv2.imshow('blurred image', image_blur)
# cv2.imshow('gray image', image_gray)
# cv2.imshow('thresholded', th1)
# cv2.imshow('sharpedned', image_sharpened)

# cv2.waitKey(0)
# cv2.destroyAllWindows()