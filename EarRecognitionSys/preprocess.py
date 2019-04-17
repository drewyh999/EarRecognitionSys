import numpy as np
import cv2


def filling(dir_path_src,dir_path_tar,datasize):
   for i in datasize:
        img = cv2.imread(dir_path_src + i +'.jpg',1)#flag > 0 to load color
        if(img.shape[0] > img.shape[1]):
            filling_size = img.shape[0]
            res_size = img.shape[1]
            background = np.zeros((filling_size, filling_size, 3), np.uint8)
            background[:, (filling_size - res_size) / 2: (filling_size - res_size) / 2 + res_size, :] = img
        else:
            filling_size = img.shape[1]
            res_size = img.shape[0]
            background = np.zeros((filling_size, filling_size, 3), np.uint8)
            background[(filling_size - res_size) / 2: res_size + (filling_size - res_size) / 2, :] = img

        cv2.resize(background, (224, 224), cv2.INTER_CUBIC)
        cv2.imwrite(dir_path_tar + i + '.jpg',background)
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



