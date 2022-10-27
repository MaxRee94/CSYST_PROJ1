import numpy as np
import cv2
# import matplotlib.pyplot as plt

def get_imagepath(timesteps, f1, f2, _lambda):
    path = "./timesteps_{},f1_{},f2_{},lambda_{}.png".format(timesteps, f1, f2, _lambda)

    return path

def write_image(arr, timesteps, f1, f2, _lambda):
    fpath = get_imagepath(timesteps, f1, f2, _lambda)
    if np.max(arr) == 1:
        arr *= 255
    cv2.imwrite(fpath, arr)

def show_image(_arr, time=0):
    arr = _arr.copy()
    arr[arr == 0] = 255
    arr[arr == 1] = 0
    length, width = arr.shape
    arr = np.reshape(arr, (length, width, 1))
    arr = np.repeat(arr, 3, axis=2)
    cv2.namedWindow('Image', cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow("Image", arr)
    cv2.waitKey(time)


if __name__ == '__main__':
    test_arr = np.random.randint(0, 2, (10000, 5000)).astype(np.float32)
    show_image(test_arr)
