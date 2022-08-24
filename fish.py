import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break
    else:
        cv2.line(img= vc, pt1= 10, pt2= 50, color ='black',thickness = 1, lineType = 8, shift = 0)
vc.release()
cv2.destroyWindow("preview")