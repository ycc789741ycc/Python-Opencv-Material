import numpy as np
import cv2

drawing = False
ix,iy=-1,-1
fx,fy=-1,-1

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,fx,fy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
        fx,fy = x,y  
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            fx,fy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx,fy = x,y   

def draw():
    img_og = np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_rectangle)

    while(1):
        img = img_og.copy()
        cv2.rectangle(img,(ix,iy),(fx,fy),(0,255,0),1)
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 :
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    draw()
