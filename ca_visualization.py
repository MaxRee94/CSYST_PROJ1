import numpy as np
import cv2
# import matplotlib.pyplot as plt


def show_image(_arr, time=0):
    _arr[_arr == 0] = 255
    _arr[_arr == 1] = 0
    length, width = _arr.shape
    _arr = np.reshape(_arr, (length, width, 1))
    _arr = np.repeat(_arr, 3, axis=2)
    cv2.imwrite('./1.png', _arr)
    cv2.namedWindow('Image', cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow("Image", _arr)
    cv2.waitKey(time)



if __name__ == '__main__':
    test_arr = np.random.randint(0, 2, (10000, 5000)).astype(np.float32)
    show_image(test_arr)
