import numpy as np
from PIL import Image


def stereo_matching_ssd(left_img, right_img, kernel_size, disparity_range):
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    height = 288
    width = 384

    depth = np.zeros((height, width), np.uint8)
    scale = 255 / disparity_range

    kernel_half = int((kernel_size - 1) / 2)

    for y in range(kernel_half, height - 1 - kernel_half):
        for x in range(kernel_half, width - 1 - kernel_half):
            cost_min = 255**2
            disparity = 0

            for j in range(disparity_range):
                cost = 0
                cost_tmp = 0
                for v in range(y - kernel_half, y + kernel_half):
                    for u in range(x - kernel_half, x + kernel_half):
                        cost_tmp = 255 * 2
                        if u - j >= 0:
                            cost_tmp = (int(left[v, u]) - int(right[v, u - j])) ** 2
                        cost += cost_tmp

                if cost < cost_min:
                    disparity = j
                    cost_min = cost

            depth[y, x] = disparity * scale
    Image.fromarray(depth).save('sm2_2.png')


if __name__ == '__main__':
    disparity_range = 16
    kernel_size = 5
    stereo_matching_ssd('left.png', 'right.png', kernel_size, disparity_range)
