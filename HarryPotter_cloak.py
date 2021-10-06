import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required = True, help = 'webcam or video from hard disk')
args = vars(ap.parse_args())

#load color_range.npy and assign these values ​​to the lower_range and upper_range
color_range = np.load('Color_range.npy')
lower_range = color_range[0]
upper_range = color_range[1]

kernel = np.ones((5,5),np.uint8)

if args["input"] == "webcam":
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(args["input"])
cap.set(3, 640)
cap.set(4, 480)

last_frame = None
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break
    
    if last_frame is None:
        last_frame = frame
        
    #convert color BGR2HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #limit colors between lower_range ​​and upper_range
    mask = cv2.inRange(hsv, lower_range, upper_range)
    
    #apply erodation for eliminate background noise
    mask = cv2.erode(mask, kernel, iterations = 1)
    
    #apply dilation for eliminate foreground noise
    mask = cv2.dilate(mask, kernel, iterations = 2)
    
    
    foreground = cv2.bitwise_and(frame, frame, mask = cv2.bitwise_not(mask))
    mask_reverse_red = cv2.bitwise_or(last_frame,foreground, mask = mask)   
    delta_frame = cv2.absdiff(foreground, mask_reverse_red)

    cv2.imshow('Invisible Cloak', delta_frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()