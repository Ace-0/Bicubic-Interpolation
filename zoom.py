import numpy as np
import math

# todo grey
def bicubic(input_img, height, width):
    (src_height, src_width, depth) = input_img.shape
    in_img = input_img.astype(np.float)
    out_img = np.zeros((height, width, 3));
    ratio_h = float(height) / float(src_height)
    ratio_w = float(width) / float(src_width)
    for i in range(height):
        for j in range(width):
            print str(i) + '/' + str(height - 1) + ' ' + str(j) + '/' + str(width - 1)
            x = i / ratio_h
            y = j / ratio_w
            x_int = int(math.floor(x))
            y_int = int(math.floor(y))

            r = g = b = 0.0
            for x_diff in range(-1, 3):
                for y_diff in range(-1, 3):
                    neib_x = x_int + x_diff
                    neib_y = y_int + y_diff
                    if neib_x < 0 or neib_x >= src_height or neib_y < 0 or neib_y >= src_width:
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


def get_padding(in_img, height, width):
    top = np.zeros((width, 3));
    down = np.zeros((width, 3));
    left = np.zeros((height, 3));
    right = np.zeros((height, 3));

    for k in range(height):
        top[k, :] = 3 * in_img[0, k, :] - 3 * in_img[1, k, :] + in_img[2, k, :]
        down[k, :] = 3 * in_img[height - 1, k, :] - 3 * in_img[height - 2, k, :] + in_img[height - 3, k, :]
        left[k, :] = 3 * in_img[k, 0, :] - 3 * in_img[k, 1, :] + in_img[k, 2, :]
        right[k, :] = 3 * in_img[k - width - 1, k, :] - 3 * in_img[k, width - 2, :] + in_img[k, width - 3, :]
    corner = np.zeros((4, 3))
    # top_left, down_left, top_right, down_right
    corner[0] = 3 * left[0, :] - 3 * left[1, :] + left[2, :]
    corner[1] = 3 * left[height - 1, :] - 3 * left[height - 2, :] + left[height - 3, :]
    corner[2] = 3 * right[0, :] - 3 * right[1, :] + right[2, :]
    corner[3] = 3 * right[width - 1, :] - 3 * right[width - 2, :] + right[width - 3, :]
    return top, down, left, right, corner