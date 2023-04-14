import cv2
import numpy as np

# Load the fabric image
fabric = cv2.imread('.jpg')

# Convert the image to grayscale
gray_fabric = cv2.cvtColor(fabric, cv2.COLOR_BGR2GRAY)


#Apply median blur filter to remove noise
median = cv2.medianBlur(gray_fabric, 5)

#Perform Canny edge detection
edges = cv2.Canny(median, 80, 150)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Initialize counters
num_defects = 0
# confidences = {}
# for c in classes:
#     confidences[c] = []

# Loop through contours and classify defects
for c in contours:
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    x, y, w, h = cv2.boundingRect(c)
    
    #detect holes
    if perimeter > 0 and (4 * 3.1415 * area) / (perimeter ** 2) > 0.75:
        cv2.drawContours(fabric, [c], -1, (255, 0, 0), 2)                   #Blue
        #cv2.rectangle(fabric, (x, y), (x+w, y+h), (0, 0, 255), 2)
        label = "Hole"
        confidence = "{:.2f}%".format(((4 * 3.1415 * area) / (perimeter ** 2)) * 100)
        cv2.putText(fabric, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)
        
    # Classify irregular contours as snags
    elif area > 100 and h / w > 2:
        #cv2.drawContours(fabric, [c], -1, (255, 0, 0), 2)
        cv2.rectangle(fabric, (x, y), (x+w, y+h), (0, 255, 0), 2)            #Green
        label = "Snags"
        confidence = "{:.2f}%".format(h / w * 100)
        cv2.putText(fabric, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)

    # Classify thin and elongated contours as extra threads
    elif area > 50 and w / h > 10:
        #cv2.drawContours(fabric, [c], -1, (0, 255, 0), 2)
        cv2.rectangle(fabric, (x, y), (x+w, y+h), (255, 255, 255), 2)        #White
        label = "Extra Threads"
        confidence = "{:.2f}%".format(w / h * 100)
        cv2.putText(fabric, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
        
    # detect weaving defects
    elif area > 100 or perimeter < 50:
        #cv2.drawContours(fabric, [c], -1, (0, 0, 255), 2)
        cv2.rectangle(fabric, (x, y), (x+w, y+h), (255, 255, 0), 2)           #skyblue
        label = "Weaving"
        confidence = "{:.2f}%".format(w / h * 100)
        cv2.putText(fabric, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)
        

# Evaluate severity of defects
if num_defects > 5:
    print("Fabric is highly defective.")
elif num_defects > 2:
    print("Fabric has moderate defects.")
else:
    print("Fabric has few defects.")


# Display the result image
cv2.imshow('Fabric with Defects', fabric)
#cv2.imshow('Fabric with Defects',median)
cv2.waitKey(0)
cv2.destroyAllWindows()