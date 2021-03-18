# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#-*-coding:gb2312-*-

import os
import xml.etree.ElementTree as ET
from sys import exit
from PIL import Image
import sys

def auto_renameclasses():
    root_path = os.getcwd() + '\\xml'
    xml_names = []
    try:
        xml_names = os.listdir(root_path)
    except FileNotFoundError as e:
        print(str(e))
        print("请把该程序放在“archive/dataset/”目录下")
        quit()
    for xmlfile in xml_names:
        doc = ET.parse(os.path.join(root_path, xmlfile))
        root = doc.getroot()
        sub1 = root.findall('object')  # 找到filename标签，
        for each in sub1:
            sub2 = each.find('name')
            if sub2.text != 'Coverall':
                string = sub2.text
                string = string.lower()
                sub2.text = string

        doc.write(os.path.join(root_path, xmlfile))  # 保存修改

def man_renameclasses():
    img_color = {}
    root_path = os.getcwd()
    img_names = []
    print('如果需要从指定图片开始请输入图片名称包括后缀，不需要则按n继续')
    image_in = input()

    try:
        img_names = os.listdir(root_path + '\\images')
    except FileNotFoundError as e:
        print(str(e))
        print("请把该程序放在“archive/dataset/”目录下")
        exit()
    for img in img_names:
        if image_in != 'n':
            if img != image_in:
                continue
            else:
                image_in = 'n'
        img_path = os.path.join(root_path + '\\images', img)

        im = Image.open(img_path)
        im.show()

        print('请按照从左到右的顺序依次标出图中的防护服颜色(b代表蓝色w代表白色),中间用空格隔开,按回车进入下一张，按q退出:')
        text = input()
        if text == 'q':
            exit()
        colors = text.split(' ')
        colors = [x.strip() for x in colors if x.strip() != '']
        img_color[img] = colors



    print('现在开始修改xml标注信息，请稍等...')
    for img in img_names:
        xml_name = img[:-4] + '.xml'
        if img in img_color.keys():
            xml_path = os.path.join(root_path + '\\xml', xml_name)
        else:
            continue

        doc = ET.parse(xml_path)
        root = doc.getroot()
        sub1 = root.findall('object')  # 找到filename标签，
        bndbox_x = []
        for each in sub1:  # 找到所有bndbox的xmin用于排序
            name = each.find('name')
            if name.text in ['Coverall', 'blue_protection', 'white_protection']:
                bndbox = each.find('bndbox')
                xmin = bndbox.find('xmin')
                bndbox_x.append(float(xmin.text))
        bndbox_x.sort()
        for x in bndbox_x:
            for each in sub1:
                name = each.find('name')
                if name.text not in ['Coverall', 'blue_protection', 'white_protection']:
                    continue
                bndbox = each.find('bndbox')
                xmin = bndbox.find('xmin')
                if float(xmin.text) == float(x):
                    if img_color[img][bndbox_x.index(x)] == 'w':
                        name.text = 'white_protection'
                    elif img_color[img][bndbox_x.index(x)] == 'b':
                        name.text = 'blue_protection'
                    else:
                        print(img + "图片的标注有问题，请重新标注")
                        with open(root_path + '\\wrong_imgs.txt', 'a+') as f:
                            f.write(img + '\n')
                    break

        doc.write(xml_path)  # 保存修改
    print('修改成功！')



if __name__ == '__main__':
    man_renameclasses()



