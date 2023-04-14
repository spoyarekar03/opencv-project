import cv2

# Load the pre-trained Cascade Classifier
classifier = cv2.CascadeClassifier("")

# Open the video file
cap = cv2.VideoCapture("video_file.mp4")

# Loop over each frame of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    
    # If the frame is not successfully read, break the loop
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect defects in the frame
    defects = classifier.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    # Loop over the detected defects and draw bounding boxes with confidence levels
    for (x, y, w, h) in defects:
        # draw bounding box with confidence level and class name
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, f"Class: Defective ", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Show the output frame with bounding boxes
    cv2.imshow("Defects Detected", frame)
    
    # Wait for 1 millisecond for a key press event
    key = cv2.waitKey(1)

    # If the 'q' key is pressed, break the loop
    if key == ord("q"):
        break

# Release the video file and destroy the window
cap.release()
cv2.destroyAllWindows()