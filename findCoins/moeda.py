import numpy as np
import cv2
import matplotlib.pyplot as plt


imageCoin = cv2.imread(r'coin.png')
imageMario = cv2.imread(r'mario.png')

grayCoin = cv2.cvtColor(imageCoin, cv2.COLOR_BGR2GRAY)
grayMario = cv2.cvtColor(imageMario, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(grayMario, grayCoin, cv2.TM_CCOEFF_NORMED)

threshold = 0.99

loc = np.where(res >= threshold)

h, w = grayCoin.shape
for pt in zip(*loc[::-1]):
    cv2.rectangle(imageMario, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

img = cv2.cvtColor(imageMario, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()