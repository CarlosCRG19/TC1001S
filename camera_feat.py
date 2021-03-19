import cv2

# Open the device at the ID 0 
cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print('Could not open video device')