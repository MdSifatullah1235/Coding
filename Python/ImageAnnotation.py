import cv2
import matplotlib.pyplot as plt


#Load the image 

img_path = "1.jpeg"
img = cv2.imread(img_path)

#Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Get image dimensions
height, width, _ = img_rgb.shape

#Draw 2 rectangles in interesting regions
#Rectangle 1: Top Left
rect1_width,rect1_height = 150,150
top_left1 = (20,20)
bottom__right = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(img_rgb, top_left1, bottom__right, (0,255,0), 2) #Yellow rectangle

#Rectangle 2: Bottom Right
rect2_width,rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom__right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(img_rgb, top_left2, bottom__right2, (255,0,255), 3) #Magenta rectangle

#Draw Circles at the center of the rectangles
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_height // 2
cv2.circle(img_rgb, (center1_x, center1_y), 5, (0,0,255), -1) #Red circle
cv2.circle(img_rgb, (center2_x, center2_y), 5, (0,255,0), -1) #Green circle

#Draw connecting lines between centers of the rectangles
cv2.line(img_rgb, (center1_x, center1_y), (center2_x, center2_y), (255,0,0), 2) #Blue line

#Add text labels for regions and centers
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_rgb, "Region 1", (top_left1[0], top_left1[1] - 10), font, 0.8, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img_rgb, "Region 2", (top_left2[0], top_left2[1] - 10), font, 0.8, (255,0,255), 2, cv2.LINE_AA)
cv2.putText(img_rgb, "Center 1", (center1_x, center1_y + 10), font, 0.8, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(img_rgb, "Center 2", (center2_x, center2_y + 10), font, 0.8, (0,255,0), 2, cv2.LINE_AA)

#Add Bi-Directional arrow representing height
arrow_start = (width -50,20)
arrow_end = (width - 50, height - 20)

#Draw arrows in both directions
cv2.arrowedLine(img_rgb, arrow_start, arrow_end, (0,0,255), 2,tipLength=0.05)
cv2.arrowedLine(img_rgb, arrow_end, arrow_start, (0,0,255), 2,tipLength=0.05)

#Annotate the height value
height_label_position = (arrow_start[0] - 150,arrow_start[1] + arrow_end[1] // 2)
cv2.putText(img_rgb, "Height", height_label_position, font, 0.8, (0,0,255), 2, cv2.LINE_AA)

#Display the annotated image
plt.imshow(img_rgb)
plt.title("Image Annotation")
plt.show()