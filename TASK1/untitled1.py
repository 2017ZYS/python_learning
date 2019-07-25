# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:26:22 2019

@author: ZYS
"""


queryIdx_3=np.array(queryIdx_list)[index].tolist()
points_query=cv2.KeyPoint_convert(kp1,queryIdx_3)

trainIdx_3=np.array(trainIdx_list)[index].tolist()
points_train=cv2.KeyPoint_convert(kp2,trainIdx_3)


cv2.circle(img1,tuple(np.rint(points_query[0,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img1,tuple(np.rint(points_query[1,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img1,tuple(np.rint(points_query[2,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img1,tuple(np.rint(points_query[3,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img1,tuple(np.rint(points_query[4,:]).astype(np.int16)),2,(255,0,0),2)
plt.figure(figsize=(10,10))
plt.imshow(img1[:,:,(2,1,0)])
plt.show()

cv2.circle(img2_resize,tuple(np.rint(points_train[0,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train[1,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train[2,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train[3,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train[4,:]).astype(np.int16)),2,(255,0,0),1)


plt.figure(figsize=(8,8))
plt.imshow(img2_resize[:,:,(2,1,0)])
plt.show()