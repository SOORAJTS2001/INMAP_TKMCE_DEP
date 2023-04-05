import cv2,numpy as np
img = cv2.imread("map.png")
pix =[]
gpix = []
img = cv2.resize(img, (200, 100))
lower_bound = np.array([0,0,202])
upper_bound = np.array([0,0,206])
pixels = np.argwhere(cv2.inRange(img,lower_bound,upper_bound))
lower_bound = np.array([6,154,78])
upper_bound = np.array([8,158,80])
green_pixels = np.argwhere(cv2.inRange(img,lower_bound,upper_bound))
for i in range(len(pixels)):
    pix.append((pixels[i][0],pixels[i][1]))
for i in range(len(green_pixels)):
    gpix.append((green_pixels[i][0],green_pixels[i][1]))
print(pix,len(pixels))
print(gpix,len(green_pixels))
# print(img.shape[0],img.shape[1])
map = open("map.txt", "w")
for i in range(1,100):
    for j in range(200):
        if (i,j) in pix:
            map.write(' ')
        elif (i,j) in gpix:
            map.write('*')
        else:
            map.write('#')
    map.write('\n')
map.close()
# for px, py in pixels:
#     print(px,py)

