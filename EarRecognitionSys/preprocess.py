import numpy as np
import cv2


def filling(dir_path,datasize):
    for i in datasize:
        img = cv2.imread(dir_path + i +'.jpg',1)#flag > 0 to load color

        if(img.cols > img.rows):
            filling_size = img.cols
            res_size = img.rows
            background = np.zeros((filling_size, filling_size, 3), np.uint8)
            background[:, (filling_size - res_size) / 2: filling_size + (filling_size - res_size) / 2] = img
        else:
            filling_size = img.rows
            res_size = img.cols
            background = np.zeros((filling_size, filling_size, 3), np.uint8)
            background[(filling_size - res_size) / 2: filling_size + (filling_size - res_size) / 2, :] = img

        cv2.resize(background, (224, 224))
        cv2.imwrite(dir_path + i +'.jpg',img)

def mean(dir_path,datasize):
    sum = np.zeros((224, 224, 3), np.uint8)
    for i in datasize:
        img = cv2.imread(dir_path + i +'.jpg',1)
        sum = cv2.add(sum, img)

    m = sum / datasize

    for i in datasize:
        img = cv2.imread(dir_path + i + '.jpg', 1)
        img = cv2.subtract(img,m)
        cv2.imwrite(dir_path + i +'.jpg',img)




