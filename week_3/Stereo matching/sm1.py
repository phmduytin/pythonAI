import math
import numpy as np
from PIL import Image


def stereo_matching(left_img, right_img, disparity_range):
    # read from left to right and convert to grayscale
    left_img = Image.open(left_img).convert('L')

    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    # Size
    height = 288
    width = 384

    depth = np.zeros((height, width), np.uint8)
    scale = 255 / disparity_range

    for y in range(height):
        for x in range(width):
            disparity = 0
            cost_min = (int(left[y, x]) - int(right[y, x])) ** 2

            for j in range(1, disparity_range):
                cost = 255 ** 2 if x + j >= width else (int(right[y, x]) - int(left[y, x + j])) ** 2
                #cost = 255 ** 2 if x - j <0 else (int(left[y, x]) - int(right[y, x - j])) ** 2

                if cost < cost_min:
                    cost_min = cost
                    disparity = j

            depth[y, x] = disparity*scale

    Image.fromarray(depth).save('depth.png')

    # print(depth)


if __name__ == '__main__':
    disparity = 16
    stereo_matching('left.png', 'right.png', disparity)
