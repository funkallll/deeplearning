#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from lxml.etree import Element, SubElement, tostring, ElementTree

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ['bottle'] # 类别

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('F:/pycharmpractice/my/datazip/ORCA-Uboat_data/FloW_IMG/FloW_IMG/test/annotations\%s.xml' % (image_id), encoding='UTF-8')

    out_file = open('F:/pycharmpractice/my/datazip/ORCA-Uboat_data/FloW_IMG/FloW_IMG/test/labels\%s.txt' % (image_id), 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        # print(cls)
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

xml_path = os.path.join(CURRENT_DIR, 'F:/pycharmpractice/my/datazip/ORCA-Uboat_data/FloW_IMG/FloW_IMG/test/annotations/')

# xml list
img_xmls = os.listdir(xml_path)
for img_xml in img_xmls:
    label_name = img_xml.split('.')[0]
    print(label_name)
    convert_annotation(label_name)
