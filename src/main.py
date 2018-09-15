import cv2
import os

import calculation
import zoom

# for filename in os.listdir('HR'):
#     img_hr = cv2.imread('HR/' + filename)
#     print filename + ' loaded from HR/'
#
#     print 'Down-sampling ' + filename + '...'
#     h_lr = img_hr.shape[0] / 3
#     w_lr = img_hr.shape[1] / 3
#     img_lr = zoom.bicubic(img_hr, w_lr, h_lr)
#
#     cv2.imwrite('LR/lr-'+ filename, img_lr)
#     print filename + ' saved as LR/lr-' + filename
#
#     print 'Up-sampling ' + filename + '...'
#     img_bi = zoom.bicubic(img_lr, img_hr.shape[1], img_hr.shape[0])
#     print img_bi.shape
#     cv2.imwrite('BI/bi-'+ filename, img_bi)
#     print filename + ' saved as BI/bi-' + filename

record = open('record.txt', 'w')

for filename in os.listdir('HR'):
    img_hr = cv2.imread('HR/' + filename)
    img_bi = cv2.imread('BI/bi-' + filename)
    line =  filename + ':\n'
    line += '\tpsnr:'+ str(calculation.PSNR(img_hr, img_bi))
    line += '\tssim:'+ str(calculation.SSIM(img_hr, img_bi))
    line += '\n\n'
    record.writelines(line)
record.close()
