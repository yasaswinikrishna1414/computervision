import cv2

image_path = r"C:\Users\grk66\OneDrive\Pictures\Saved Pictures\watch-cascade.xml"
image = cv2.imread(image_path)
# Load the Haarcascades classifier for watches
watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_watch.xml')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches in the image
watches = watch_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not loaded properly.")
