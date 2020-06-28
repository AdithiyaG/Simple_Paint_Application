import cv2.cv2 as cv
import numpy as np


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def nothing(x):
    pass
def draw(event,x,y,flags,p):
    global ix,iy,drawing,mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),p[0],-1)
            else:
                cv.circle(img,(x,y),p[1],p[0],-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

def get_values(event,x,y,flags,param):
    global ix,iy,drawing,mode

    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    radius=cv.getTrackbarPos('Radius','image')

    if s == 0:
        p=[(255,255,255),5]
        draw(event,x,y,flags,p)
    else:
        p=[(b,g,r),radius]
        draw(event,x,y,flags,p)


# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')



# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('Radius','image',0,50,nothing)
# create switch for ON/OFF functionality
switch = "ON:1"
cv.createTrackbar(switch, 'image',0,1,nothing)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Choose colors and Radius for circle by dragging "On Trackbar" to 1 ',(1,20), font, 0.45,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Click "m" to choose circle/rectangle and "c" for clear screen ',(1,297), font, 0.5,(255,255,255),2,cv.LINE_AA)


while(1):
    
    #param=values()
    cv.setMouseCallback('image',get_values)

    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    if k == ord('m'):
        mode = not mode
    elif k == ord('c'):
        img = np.zeros((300,512,3), np.uint8)

cv.destroyAllWindows()