'''###
By executing the following code, you can create 
an acceptable mask according to the color of your 
desired cape.
#################################################
Finally by finding the right values ​​for 
lower_range and upper_range save these values 
​​by pressing the 's' key.
###'''

import cv2
import numpy as np


def nothing():
    pass

cap = cv2.VideoCapture(0)


cv2.namedWindow('Trackbars')

cv2.createTrackbar('L-H', 'Trackbars',0 ,179 ,nothing)
cv2.createTrackbar('L-S', 'Trackbars',0 ,255 ,nothing)
cv2.createTrackbar('L-V', 'Trackbars',0 ,255 ,nothing)
cv2.createTrackbar('U-H', 'Trackbars',179 ,179 ,nothing)
cv2.createTrackbar('U-S', 'Trackbars',255 ,255 ,nothing )
cv2.createTrackbar('U-V', 'Trackbars',255 ,255 ,nothing )

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos('L-H', 'Trackbars')
    l_s = cv2.getTrackbarPos('L-S', 'Trackbars')
    l_v = cv2.getTrackbarPos('L-V', 'Trackbars')
    u_h = cv2.getTrackbarPos('U-H', 'Trackbars')
    u_s = cv2.getTrackbarPos('U-S', 'Trackbars')
    u_v = cv2.getTrackbarPos('U-V', 'Trackbars')
    
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    
    res = cv2.bitwise_and(frame, frame, mask = mask1)
    
    mask2 = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)
    
    stacked = np.hstack((mask2, frame, res))   
    
    cv2.imshow('Trackbars',cv2.resize(stacked, (1200,180), fx = 0.4, fy = 0.4))
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord('s'):
        ColorRange = [[l_h, l_s, l_v], [u_h, u_s, u_v]]
        print(thearray)
        
        np.save('Color_range', ColorRange)
        break
cap.release()
cv2.destroyAllWindows()
    
    