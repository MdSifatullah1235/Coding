import cv2

#Load the image 
img = cv2.imread('1.jpg')

#Convert to image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Resize the img to 224x224
resized_img = cv2.resize(gray, (224, 224))

#Display the resized grayscale image in a single window 
cv2.imshow("Processed Image", resized_img)

#Wait for a key press
key = cv2.waitKey(0) #Wait indefinitely for a key press

#Check if the "S" key was pressed
if key == ord("s"): #ord("s") returns the ASCII value of "s"
    #Save the processed image when the "s" key is pressed
    cv2.imwrite("processed_image.jpg", resized_img)
    print("Processed image saved as processed_image.jpg")
else:
    print("Processed image not saved")

#Close the window
cv2.destroyAllWindows()