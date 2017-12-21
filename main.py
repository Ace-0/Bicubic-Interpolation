import cv2
import os

import calculation
import zoom

for filename in os.listdir('HR'):
    img_hr = cv2.imread('HR/' + filename)
    print filename + ' loaded from HR/'

    print 'Down-sampling ' + filename + '...'
    h_lr = img_hr.shape[0] / 3
    w_lr = img_hr.shape[1] / 3
    img_lr = zoom.bicubic(img_hr, w_lr, h_lr)

    cv2.imwrite('LR/lr-'+ filename, img_lr)
    print filename + ' saved as LR/lr-' + filename

    print 'Up-sampling ' + filename + '...'
    img_bi = zoom.bicubic(img_lr, img_hr.shape[1], img_hr.shape[0])
    print img_bi.shape
    cv2.imwrite('BI/bi-'+ filename, img_bi)
    print filename + ' saved as BI/bi-' + filename

# print calculation.PSNR(img1, img1)
# print calculation.SSIM(img1, img1)

# bicubic(width, height)
# img_small = zoom.bicubic(img1, 800, 800)
# cv2.imwrite("big1.bmp", img_small)
