import cv2
import os
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
path='/media/y00/U393/dataset/VOC2007/JPEGImages'
xml_source_path='/media/y00/U393/dataset/VOC2007/Annotations'
txt_source_path='/media/y00/U393/dataset/VOC2007/labels'
save_path='/home/y00/ratio'
output='anno'
def readimg():
    files=os.listdir(path)
    image_list=[]
    for file in files:
        image=cv2.imread(os.path.join(path,file))
        image_list.append(image)
    return image_list
def ratio(list, hope_slide):
    new_image=[]
    for i,img in enumerate(list):
        w=list[i].shape[1]
        h=list[i].shape[0]
        scale=hope_slide/min(w,h)
        new_w=int(w*scale)
        new_h=int(h*scale)
        image_process=cv2.resize(list[i], (new_w, new_h))
        new_image.append(image_process)
        cv2.imwrite(save_path+'/'+'0000'+str(i+1)+'.jpg',image_process)
    return new_image,scale
def read_xml(files):
    xml_list=[]
    for xml in os.listdir(files):
        path=os.path.join(xml_source_path,xml)
        # source_xml=minidom.parse(path)
        xml_list.append(path)
    return xml_list

def ratio_xml(xml_list,scale):
    for i,xml_source in enumerate(xml_list):
        tree=ET.parse(xml_list[i])
        root=tree.getroot()
        # print(root[0])
        # owner=root.findall('owner')
        # print(owner[0])
        #print(root)
        # image_size_xml=xml_list[i].getElementsByTagName('size')
        image_size_xml=root.find('size')
        #image_size_xml[0].
        #print(image_size_xml)
        image_width=image_size_xml.find('width')
        image_w=int(image_width.text)
        img_w=int(image_w*scale)
        image_height=image_size_xml.find('height')
        image_h=int(image_height.text)
        img_h=int(image_h*scale)
        image_width.text=str(img_w)
        image_height.text=str(img_h)
        objects=root.findall('object')
        for idx,object in enumerate(objects):
            bndbox=object.find('bndbox')
            xmin=bndbox.find('xmin')
            xmax=bndbox.find('xmax')
            ymin=bndbox.find('ymin')
            ymax=bndbox.find('ymax')
            if 0<int(xmin.text)<1 and  0<int(ymin.text)<1 and 0<int(ymin.text)<1 and 0<int(ymax.text)<1:
                 continue
            xmin.text=str(int(int(xmin.text)*scale))
            xmax.text = str(int(int(xmax.text) * scale))
            ymin.text = str(int(int(ymin.text) * scale))
            ymax.text = str(int(int(ymax.text) * scale))
        save_anno_path=os.path.join(save_path,output,'00000'+str(i+1)+'.xml')
        tree.write(save_anno_path,method='xml',encoding='utf-8')
        #print(objects)
        #width=ET.fromstring
        #print(width)
        #image_width_xml=image_size_xml.firstChild
        #image_height_xml=image_size_xml.getElementsByTagName('height')
        #image_width=int(float(image_width_xml[0].firstChild.data))
        #image_height = int(float(image_width_xml[0].firstChild.data))
        #image_width=round(image_width*scale)
        #image_height=round(image_height*scale)
        #image_height_xml.text=str(round(image_height*scale))
        # objects=root.getElementsByTagName("bndbox")
        # for object in objects:
        #     xmin=object.getElementsByTagName("xmin")
        #     #xmin_data=xmin
        #     xmax=object.getElementsByTagName("xmax")
        #     ymin=object.getElementsByTagName("ymin")
        #     ymax=object.getElementsByTagName("ymax")
        #print(objects)
def read_txt_ratio():
    # txt_list=[]
    labels=[]
    file_list = os.listdir(txt_source_path)
    for txt in file_list:
        #print(txt)
        txt_path=os.path.join(txt_source_path, txt)
        t=open(txt_path, 'r').readlines()
        labels = [f.strip('\n').strip().split() for f in t]
        print(t)
        #print(t)
        # for lines in t:
        #     label=lines.split('\n')[0].split(' ')
        #     labels.append(label)
        #     print(labels)
    return labels
def ratio_txt(labels,scale):
    for la in labels:
        xmin=float(la[0])
        ymin=float(la[1])
        xmax=float(la[2])
        ymax=float(la[3])
        # if 0<xmin<1 and 0<ymin<1 and 0<xmax<1 and 0<ymax<1:
        #     continue
        #xmin=int(xmin*scale)


def main():
    imagelist=readimg()
    new_image,scale=ratio(imagelist,50)
    xml_list=read_xml(xml_source_path)
    ratio_xml(xml_list,scale)
    # labels=read_txt_ratio()
    # ratio_txt(labels,0.5)
if __name__ == '__main__':
    main()
