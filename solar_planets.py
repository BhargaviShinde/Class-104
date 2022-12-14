import cv2
img = cv2.imread('solar-system.jpg')
cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mercury", (110,190), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,175), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (310,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (400,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (550,70), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (800,315), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (970,115), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1145,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg',img)