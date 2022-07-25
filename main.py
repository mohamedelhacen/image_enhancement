import cv2
from outils import contrast_enhancement, blurring_image, image_thresholding, image_sharpening

image = cv2.imread('book.jpg')

image_contrast = contrast_enhancement(image)
image_blur = blurring_image(image)
thresholded = image_thresholding(image)
image_sharpened = image_sharpening(image)

cv2.imshow('Color input image', image)
cv2.imshow("histogram equalized", image_contrast)
cv2.imshow('blurred image', image_blur)
# cv2.imshow('gray image', image_gray)
cv2.imshow('thresholded', thresholded)
cv2.imshow('sharpedned', image_sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()