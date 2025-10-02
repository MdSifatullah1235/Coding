import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Example.png')

#Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.show()

#Convert to Grayscale
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_grayscale, cmap='gray')
plt.title("Grayscale Image")
plt.show()

#Cropping the image 
#Assume we know what regions we want rows 100 to 300 columns 200 to 400
cropped_img = img[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()
