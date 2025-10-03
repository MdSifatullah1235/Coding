import cv2 

#Load the image 
img = cv2.imread('Example.png')

#Resize the image into 3 different sizes
small_img = cv2.imread("Example.png",(150,150))
medium_img = cv2.imread("Example.png",(400,400))
large_img = cv2.imread("Example.png",(800,800))


cv2.namedWindow("Loaded image",cv2.WINDOW_NORMAL) #Create a resizable window 
cv2.resizeWindow("Loaded image", 1000,1000) #Resize the window to a specific size

cv2.imshow("Loaded image", small_img)
cv2.imshow("Loaded image", medium_img)
cv2.imshow("Loaded image", large_img)

cv2.waitKey(0)
cv2.destroyAllWindows()