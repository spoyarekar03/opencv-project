import cv2

# Load the video file
cap = cv2.VideoCapture(".mp4")

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3, L2gradient=True)
    
    # Find contours in the image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through the contours and classify them as defects or non-defective fabric
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        
        # Compute the perimeter of the contour
        perimeter = cv2.arcLength(cnt, True)
        
        # Compute the circularity of the contour
        circularity = 4 * 3.14 * area / (perimeter * perimeter)
        
        # Classify the contour based on circularity
        if circularity < 0.5:
            # Holes or cuts
            cv2.drawContours(frame, [cnt], 0, (0, 0, 255), 2)
        elif circularity < 0.8:
            # Snags or weaving
            cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
        else:
            # Non-defective fabric
            cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 2)
    
    # Write the frame to the output video file
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()