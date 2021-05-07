#!/home/drk/anaconda3/bin/python
import numpy as np
import cv2 as cv
import math
import time
img = np.zeros((720,1048,3), np.uint8)
cv.namedWindow('image')
font = cv.FONT_HERSHEY_SIMPLEX
while(1):
	cv.imshow("image",img)
	cv.putText(img,"Welcome Welcome ",(200,350),font,2,(142,251,42),3,cv.LINE_AA)
	cv.putText(img,"Press S to Start",(400,500),font,1,(42,251,142),1,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == ord("s"):
		img = np.zeros((720,1048,3), np.uint8)
		break
while(1):
	cv.imshow("image",img)
	cv.putText(img,"You Have to draw any cool",(20,350),font,2,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"shape, using Circle, Rectangle, Lines, Brush and more ",(50,400),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"Press Space to Continue",(70,600),font,1,(42,251,142),1,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == 32:
		img = np.zeros((720,1048,3), np.uint8)*255
		break
while(1):
	cv.imshow("image",img)
	cv.putText(img,"TIPS",(20,350),font,2,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"1. First Change the Canvas Color and then draw on it",(50,400),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"2. Use canvas color brush in mode 4 to erase",(50,500),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"Press Space to Continue",(70,600),font,1,(42,251,142),1,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == 32:
		img = np.ones((720,1048,3), np.uint8)*255
		break
drawing = False
mode = True
ix,iy = -1,-1
b,g,r = (0,0,0)
t = 1
b3,g3,r3=(0,0,0)
def nothing(x):
    pass
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
switch = 'Draw: 0 \n Canvas:1'
cv.createTrackbar(switch,'image',0,1,nothing)
cv.createTrackbar('T','image',1,500,nothing)
cv.createTrackbar('M','image',0,6,nothing)
def trackbar():
	global b,g,r,t,b1,g1,r1,t1,b2,g2,r2,t2,b3,g3,r3,s,mode
	s = cv.getTrackbarPos(switch,'image')
	if s==0:
		r = cv.getTrackbarPos('R','image')
		g = cv.getTrackbarPos('G','image')
		b = cv.getTrackbarPos('B','image')
		t = cv.getTrackbarPos('T','image')
		mode = cv.getTrackbarPos('M','image')
	elif s==1:
		r3 = cv.getTrackbarPos('R','image')
		g3 = cv.getTrackbarPos('G','image')
		b3 = cv.getTrackbarPos('B','image')
		img[50:670,20:1030]=[b3,g3,r3]
def draw_func(event,x,y,flags,param):
	global ix,iy,drawing,mode
	if event == cv.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == 0:
				cv.rectangle(img,(ix,iy),(ix,iy),(b,g,r),t)
			elif mode == 1:
				t1=t
				if t1==0:
					t1=1
				cv.line(img,(ix,y),(x,iy),(b,g,r),t1)
			elif mode == 2:
				radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
				cv.circle(img,(ix,iy),radius,(b,g,r),t)
			elif mode == 4 :
				cv.circle(img,(x,y),t,(b,g,r),-1)
			elif mode == 5:
				radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
				cv.circle(img,(x,y),radius,(b,g,r),t)
			elif mode == 6 :
				cv.circle(img,(x,y),t,(b3,g3,r3),-1)
	elif event == cv.EVENT_LBUTTONUP:
		drawing = False
		if mode == 0:
			cv.rectangle(img,(ix,iy),(x,y),(b,g,r),t)
		elif mode == 1:
			pass
		elif mode == 2:
			radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
			cv.circle(img,(ix,iy),radius,(b,g,r),t)
		elif mode == 3:
			radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
			cv.circle(img,(ix,iy),radius,(b,g,r),t)
		elif mode == 4:
			cv.circle(img,(x,y),t,(b,g,r),-1)
		elif mode == 5:
			pass
		elif mode == 6:
			cv.circle(img,(x,y),t,(b3,g3,r3),-1)
while(1):
	cv.rectangle(img,(20,50),(1030,670),(153,241,25),1)
	cv.putText(img,"JUST     DRAW     IT   MAN",(315,40),font,0.8,(255,0,0),1,cv.LINE_AA)
	cv.putText(img,"Press ESC to Get OUT",(20,700),font,1,(42,251,12),0,cv.LINE_AA)
	cv.putText(img,"Press T for Tips",(20,40),font,1,(42,251,12),0,cv.LINE_AA)
	cv.putText(img,"Press R to Reset",(710,40),font,1,(42,251,12),0,cv.LINE_AA)
	cv.imshow("image",img)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	elif k == ord('r'):
		img = np.ones((720,1048,3), np.uint8)*255
	elif k == ord('t'):
		while(1):
			cv.imshow("image",img)
			cv.putText(img,"TIPS",(20,350),font,2,(142,251,42),1,cv.LINE_AA)
			cv.putText(img,"1. First Change the Canvas Color and then draw on it",(50,400),font,1,(142,251,42),1,cv.LINE_AA)
			cv.putText(img,"2. Use canvas color brush in mode 4 to erase",(50,500),font,1,(142,251,42),1,cv.LINE_AA)
			cv.putText(img,"Press Space to Continue",(70,600),font,1,(42,251,142),1,cv.LINE_AA)
			if cv.waitKey(1) & 0xFF == 32:
				img = np.ones((720,1048,3), np.uint8)*255
				break
	trackbar()
	cv.setMouseCallback("image", draw_func)
cv.destroyAllWindows()
