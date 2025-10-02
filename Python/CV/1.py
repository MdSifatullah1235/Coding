import cv2

#Load the image 
img = cv2.imread('1.jpg')

#Resize the window to a specific size witthout resizing the image

cv2.namedWindow("Loaded image",cv2.WINDOW_NORMAL) #Create a resizable window 
cv2.resizeWindow("Loaded image", 800,500) #Resize the window to a specific size

#Display the img in the resized window
cv2.imshow("Loaded image", img)
cv2.waitKey(0) #Wait for a key press
cv2.destroyAllWindows() #Close the window

#Print image properties
print(f"Image Dimensions : {img.shape}") #Height,Width,Channels