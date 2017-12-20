import numpy as np
import math

# todo grey
def bicubic(input_img, width, height):
    (src_width, src_height, depth) = input_img.shape
    in_img = input_img.astype(np.float)
    out_img = np.zeros((width, height, 3));
    ratio_w = float(width) / float(src_width)
    ratio_h = float(height) / float(src_height)
    for i in range(width):
        for j in range(height):
            print str(i) + '/' + str(width - 1) + ' ' + str(j) + '/' + str(height - 1)
            x = i / ratio_w
            y = j / ratio_h
            x_int = int(math.floor(x))
            y_int = int(math.floor(y))

            r = g = b = 0.0
            for x_diff in range(-1, 3):
                for y_diff in range(-1, 3):
                    neib_x = x_int + x_diff
                    neib_y = y_int + y_diff
                    if neib_x < 0 or neib_x >= src_width or neib_y < 0 or neib_y >= src_height:
                        continue
                    out_img[i, j, :] += in_img[neib_x, neib_y, :] * get_weight(x - neib_x) * get_weight(y - neib_y)

    out_img = np.around(out_img)
    return out_img


def get_weight(distance):
    dis = abs(distance)
    if 0 <= dis <= 1:
        return 1.5 * pow(dis, 3) - 2.5 * pow(dis, 2) + 1
    elif 1 < dis <= 2:
        return 0 - 0.5 * pow(dis, 3) + 2.5 * pow(dis, 2) - 4 * dis + 2
    else:
        return 0


def get_prediction(x, y, pixel):
    width = len(pixel)
    height = len(pixel[0])
    left_pred = right_pred = up_pred = down_pred = []
    for k in range(height + 1):
        r = 3 * pixel[0, k][0] - 3 * pixel[1, k][0] + pixel[2, k][0]
        g = 3 * pixel[0, k][1] - 3 * pixel[1, k][1] + pixel[2, k][1]
        b = 3 * pixel[0, k][2] - 3 * pixel[1, k][2] + pixel[2, k][2]
        left_pred.append((r, g, b))
    for k in range(height + 1):
        r = 3 * pixel[width - 1, k][0] - 3 * pixel[width - 2, k][0] + pixel[width - 3, k][0]
        g = 3 * pixel[width - 1, k][1] - 3 * pixel[width - 2, k][1] + pixel[width - 3, k][1]
        b = 3 * pixel[width - 1, k][2] - 3 * pixel[width - 2, k][2] + pixel[width - 3, k][2]
        right_pred.append((r, g, b))

    if i == -1 and j == -1:
        return 3 * pixel[0, -1] - 3 * pixel[1, -1] + pixel[2, -1]
    elif i == -1 and j == height:
        return 3 * pixel[0, height - 1] - 3 * pixel[1, -1] + pixel[2, -1]
