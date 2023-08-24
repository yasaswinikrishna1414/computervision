import cv2

img = cv2.imread(r"C:\Users\grk66\OneDrive\Pictures\Saved Pictures\sky.jpg")
cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
