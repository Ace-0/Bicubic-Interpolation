import numpy as np
import scipy.ndimage as spnd
import math
import cv2


def PSNR(img1, img2):
    if img1.shape != img2.shape:
        raise Exception("The sizes of two images cannot be different")
    if img1.ndim == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCR_CB)
    img1 = img1[:,:,0].astype(np.float)
    img2 = img2[:,:,0].astype(np.float)
    mse = get_mse(img1, img2)
    if mse == 0:
        return float('inf')
    level = 255 - 16
    psnr = 20 * math.log(level / math.sqrt(mse), 10)
    return psnr


def get_mse(img1, img2):
    diff = img1 - img2
    mse = np.mean(np.square(diff))
    return mse


def SSIM(img1, img2):
    if img1.shape != img2.shape:
        raise Exception("The sizes of two images cannot be different")
    if img1.ndim == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCR_CB)
    img1 = img1[:,:,0].astype(np.float)
    img2 = img2[:,:,0].astype(np.float)
    k = [0.01, 0.03];
    level = 255 - 16;
    window = gauss_2d((11, 11), 1.5)
    window /= np.sum(window)

    mu1 = spnd.filters.convolve(img1, window)
    mu2 = spnd.filters.convolve(img2, window)
    sigma1_sq = spnd.filters.convolve(img1**2, window) - mu1**2
    sigma2_sq = spnd.filters.convolve(img2**2, window) - mu2**2
    sigma12 = spnd.filters.convolve(img1 * img2, window) - mu1 * mu2
    c1 = pow(k[0] * level, 2)
    c2 = pow(k[1] * level, 2)

    up = (2 * mu1 * mu2 + c1) * (2 * sigma12 + c2)
    down = (mu1 * mu1 + mu2 * mu2 + c1) * (sigma1_sq + sigma2_sq + c2)
    ssim = np.mean(up / down)
    return ssim

def gauss_2d(shape, sigma):
    # Code from Stack Overflow's thread
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m+1, -n:n+1]
    h = np.exp(-(x*x + y*y) / (2.*sigma*sigma))
    h[h < np.finfo(h.dtype).eps*h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h