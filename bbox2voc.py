import cv2,os
import numpy as np
import glob
from PIL import Image

src_img_dir = "./VOC/JPEGImages"
src_xml_dir = "./VOC/Annotations"
width, height=512,512


for i in os.listdir("./label/"):
    ii='./label/'+i
    a=cv2.imread(ii,0)
    _,contours, hierarchy = cv2.findContours(a,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    xml_file = open((src_xml_dir + '/' + i[:-4] + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + i + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        print (i[0],i,x, y, x+w, y+h)
        if i[0]=='1':
            name='class32342'
        xml_file.write('    <object>\n')
        xml_file.write('        <name>' + name + '</name>\n')
        xml_file.write('        <pose>Unspecified</pose>\n')
        xml_file.write('        <truncated>0</truncated>\n')
        xml_file.write('        <difficult>0</difficult>\n')
        xml_file.write('        <bndbox>\n')
        xml_file.write('            <xmin>' + str(x) + '</xmin>\n')
        xml_file.write('            <ymin>' + str(y) + '</ymin>\n')
        xml_file.write('            <xmax>' + str(x+w) + '</xmax>\n')
        xml_file.write('            <ymax>' + str(y+h) + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')

    xml_file.write('</annotation>')
