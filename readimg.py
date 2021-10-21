import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
path=''
path1='rgb'
path2='cam0'
output = "output"
import time
from tqdm import tqdm

def readimg():
    array_img = []
    image_path=[]
    files=os.listdir(path)
    #print(files)
    for file in tqdm(files):
        path_1=os.path.join(path,file)
        if ".txt" in path_1:
            continue
        #print(path_1)
        img_path=os.path.join(path_1,path1,path2)
        img_file=os.listdir(img_path)
        image_path.append(file)
        #print(img_path)
        for i,f in enumerate(img_file):
            if i%20==0:
                image=cv2.imread(img_path+'/'+f,cv2.IMREAD_GRAYSCALE)
                equ_image=cv2.equalizeHist(image)
                # image=resizeimg(img,1)-215:Assertion failed) _src.type() == CV_8UC1 in function 'equalizeHist
                array_img.append(equ_image)
                if len(array_img)==6:
                    imshowimg(array_img, img_path)
                    array_img = []
    return array_img,image_path

#readimg()
def imshowimg(array_img,image_path):
    image1 = np.hstack(array_img[0:3])
    image2 = np.hstack(array_img[3:6])
    image = np.vstack((image1, image2))
    image = cv2.resize(image,(1720,960))
    # cv2.namedWindow(image_path)
    # cv2.imshow(image_path, image)
    # cv2.waitKey(0)
    # cv2.destroyWindow(image_path)
    path = os.path.join(output, image_path.split("REMAP/")[-1].split("/gray")[0] + "_" + str(time.time())) + ".jpg"
    #path=os.path.join(output1,image_path.split('/')[7],str(time.time()))+".jpg"
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    cv2.imwrite(path, image)
    return
    # for i in range(0,len(array_img),6):
    #     #print(len(array_img))
    #     plt.figure(figsize=(18, 10))
    #     plt.subplot(2,3,1)
    #     plt.imshow(array_img[i])
    #     plt.subplot(2,3,2)
    #     plt.imshow(array_img[i+1])
    #     plt.subplot(2,3,3)
    #     plt.imshow(array_img[i+2])
    #     plt.subplot(2,3,4)
    #     plt.imshow(array_img[i+3])
    #     plt.subplot(2,3,5)
    #     plt.imshow(array_img[i+4])
    #     plt.subplot(2,3,6)
    #     plt.imshow(array_img[i+5])
    #     plt.show()
    #     # for i in enumerate(image_path[i]):
    #     #
    #     #     plt.xlabel(image_path[i])



def resizeimg(img,scale):
    h,w=img.shape[0],img.shape[1]
    new_h=int(h*scale)
    new_w=int(w*scale)
    image=cv2.resize(img,(new_w,new_h))

    return image

def main():
    array,imagepath=readimg()
    # imshowimg(array_img=array,image_path=imagepath)
    #pass
if __name__ == '__main__':
    main()

