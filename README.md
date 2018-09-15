# Bicubic Interpolation

Simple implementation of Bicubic-Interpolation

Reference Paper: [Cubic convolution interpolation for digital image processing](./doc/Cubic_convolution_interpolation_for_digital_image_processing.pdf)

### Example

low resolution image

![](./low-resolution-examples/lr-lenna.bmp)

original high-resolution image

![](./high-resolution-examples/lenna.bmp)

result of bicubic interpolation

![](./bicubic-examples/bi-lenna.bmp)


### Comparison

Comparison between **original high-resolution images** and **results of bicubic interpolation**

|  Image  |  PSNR   |  SSIM  |
| :-----: | :-----: | :----: |
| baboon  | 20.2090 | 0.5161 |
|  lenna  | 30.0443 | 0.8705 |
|   man   | 24.7873 | 0.7309 |
| monarch | 27.7529 | 0.9212 |
| pepper  | 29.3691 | 0.8732 |


