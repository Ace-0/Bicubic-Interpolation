import numpy as np
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
    level = 255
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
    level = 255;
    window = gaussion_kernal((11, 11), 1.5)
    window /= np.sum(window)

    mu1 = conv(img1, window)
    mu2 = conv(img2, window)
    cv2.imwrite('test.bmp', mu1)
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu_12 = mu1 * mu2
    sigma1_sq = conv(img1**2, window) - mu1_sq
    sigma2_sq = conv(img2**2, window) - mu2_sq
    sigma12 = conv(img1 * img2, window) - mu_12
    c1 = pow(k[0] * level, 2)
    c2 = pow(k[1] * level, 2)

    up = (2 * mu_12 + c1) * (2 * sigma12 + c2)
    down = (mu1_sq + mu2_sq + c1) * (sigma1_sq + sigma2_sq + c2)
    ssim = np.mean(up / down)
    return ssim


def gaussion_kernal(shape, sigma):
    k = shape[0] / 2
    kernal = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            evalue = - (((i - k - 1)**2 + (j - k - 1)**2) / (2 * sigma**2))
            divalue = 2 * math.pi * sigma**2
            kernal[i, j] = math.exp(evalue) / divalue
    return kernal

def conv(img, filter):
    out_img = np.zeros(img.shape)
    half = filter.shape[0] / 2
    for i in range(half, img.shape[0] - half):
        for j in range(half, img.shape[1] - half):
            patch = img[i - half:i + half + 1, j - half:j + half + 1] * filter
            out_img[i, j] = patch.sum()

    return np.round(out_img[half:img.shape[0] - half, half:img.shape[1] - half])