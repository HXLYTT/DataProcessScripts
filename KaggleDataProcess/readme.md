# kaggle防护服数据集的防护服颜色区分脚本

## 介绍
[Kaggle](https://www.kaggle.com/ialimustufa/object-detection-for-ppe-covid19-dataset)上有已经标注过的一些防护服图片。[标注工具链接](https://github.com/tzutalin/labelImg/releases/tag/v1.8.1)

标注格式：仿照上面的数据集，使用VOC格式。class有Gloves、Mask、Face_Shield、Goggles、Coverall 5类

由于项目需求需要区分防护服颜色即上述Coverall，因此写了该脚本人工标记防护服颜色，按从左到右顺序输入颜色首字母即可(这里只有两类：蓝色和白色，用b和w表示)

## 用法

将脚本放在'archieve/dataset/'目录下，控制台运行脚本即可（脚本运行后附带具体标注教程）

~~~
./anna_color.exe
~~~

ps:由于kaggle的防护服数据集做过改名和移动的预处理，对应目录如下

~~~ dataset
  dataset
     |——images
     |——xml 
~~~

## 注意事项

1. 由于技术问题，使用脚本时会自动弹出对应的照片但无法关闭，需要**手动关闭**
2. 如果遇到标注有误的需要重新标注，会有提示，同时出错的照片名称保存在当前目录下的wrong_imgs.txt中，</br>再次运行脚本选择从指定照片标注即可；若错误照片并非连续则需要标注一张后退出然后再次运行选择从指定照片标注。


