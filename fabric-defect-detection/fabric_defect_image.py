import cv2

# Load the input image
img = cv2.imread("positive/56.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the pre-trained Cascade Classifier
classifier = cv2.CascadeClassifier("required_files/cascade_level02")

# Detect defects in the image
max_size = (512, 512)
defects = classifier.detectMultiScale(gray, scaleFactor=3.05, minNeighbors=3, maxSize=max_size)

# Loop over the detected defects and draw bounding boxes with confidence levels
for (x, y, w, h) in defects:
    # draw bounding box with confidence level and class name
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(img, f"Class: Defective ", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# Show the output image with bounding boxes
cv2.imshow("Defects Detected", img)
cv2.waitKey(0)