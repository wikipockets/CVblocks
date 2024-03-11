import cv2
import numpy as np

# read  image
img = cv2.imread('game2.jpg')

# read template with alpha channel
template_with_alpha = cv2.imread('game_template.png', cv2.IMREAD_UNCHANGED)
hh, ww = template_with_alpha.shape[:2]

# extract base template image and alpha channel and make alpha 3 channels
template = template_with_alpha[:,:,0:3]
alpha = template_with_alpha[:,:,3]
alpha = cv2.merge([alpha,alpha,alpha])

# do masked template matching and save correlation image
correlation = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED, mask=alpha)

# get best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(correlation)
max_val_corr = '{:.6f}'.format(max_val)
print("correlation score: " + max_val_corr)
print("match location:", max_loc)

# draw match
result = img.copy()
cv2.rectangle(result, (max_loc), ( max_loc[0]+ww,  max_loc[1]+hh), (0,0,255), 1)

# save results
cv2.imwrite('game2_matches.jpg', result)

cv2.imshow('template',template)
cv2.imshow('alpha',alpha)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()