import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_filters(img,filter_type):
    filtered_img = img.copy()
    
    if filter_type == "red_tint":
        filtered_img[:,:,1] = 0 #green channel to 0
        filtered_img[:,:,0] = 0 #blue channel to 0
        filtered_img[:,:,2] = filter_input
    
    elif filter_type == "green_tint":
        filtered_img[:,:,0] = 0 #blue channel to 0
        filtered_img[:,:,2] = 0 #red channel to 0
        filtered_img[:,:,1] = filter_input

    elif filter_type == "blue_tint":
        filtered_img[:,:,1] = 0 #green channel to 0
        filtered_img[:,:,2] = 0 #red channel to 0
        filtered_img[:,:,0] = filter_input
    
    elif filter_type == "sobel":
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
        filtered_img = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    
    elif filter_type == "black":
        filtered_img[:,:,0] = 0
        filtered_img[:,:,1] = 0
        filtered_img[:,:,2] = 0
    
    elif filter_type == "white":
        filtered_img[:,:,0] = 255
        filtered_img[:,:,1] = 255
        filtered_img[:,:,2] = 255
    
    elif filter_type == 'canny':
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_img, 100, 200)
        filtered_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return filtered_img

image_path = "Example2.jpeg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: {image_path} is not found.")

else: 
    filter_type = "original" #Defualt image

    print("Press the folollowing keys to apply filters: ")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit the program")

    while True:
        filtered_image = apply_filters(img,filter_type)


        #Wait for a key press
        key = cv2.waitKey(0) & 0xFF
        if key == ord("r"):
            filter_input = int(input("Enter the filter input: "))
            filter_type = "red_tint"
            show_choice_input = input("Do you want to see the filtered image? (y/n) :")
            if show_choice_input == "y":
                cv2.imshow("Filtered Image",filtered_image)
        elif key == ord("g"):
            filter_input = int(input("Enter the filter input: "))
            filter_type = "green_tint"
            show_choice_input = input("Do you want to see the filtered image? (y/n) :")
            if show_choice_input == "y":
                cv2.imshow("Filtered Image",filtered_image)
        elif key == ord("b"):
            filter_input = int(input("Enter the filter input: "))
            filter_type = "blue_tint"
            show_choice_input = input("Do you want to see the filtered image? (y/n) :")
            if show_choice_input == "y":
                cv2.imshow("Filtered Image",filtered_image)
        elif key == ord("s"):
            filter_type = "sobel"
            show_choice_input = input("Do you want to see the filtered image? (y/n) :")
            if show_choice_input == "y":
                cv2.imshow("Filtered Image",filtered_image)
        elif key == ord("c"):
            filter_type = "canny"
            how_choice_input = input("Do you want to see the filtered image? (y/n) :")
            if show_choice_input == "y":
                cv2.imshow("Filtered Image",filtered_image)
        elif key == ord("q"):
            print("Exiting the program...")
            break

cv2.destroyAllWindows()