import cv2
import calculation
import zoom

img1 = cv2.imread("Set14/bridge.bmp")
img2 = cv2.imread("Set14/lenna.bmp")
img3 = cv2.imread("Set14/pepper.bmp")
img4 = cv2.imread("Set14/man.bmp")
img5 = cv2.imread("Set14/baboon.bmp")

# print calculation.PSNR(img2, img3)
# print calculation.SSIM(img2, img3)

img_small = zoom.bicubic(img5, 700, 700)
cv2.imwrite("big5.bmp", img_small)
