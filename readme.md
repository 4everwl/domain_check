## 简介

使用python3编写的一个批量查询网站权重的小工具。通过批量txt文件，将最终的结果输出为txt文件，目前只包含百度，移动，谷歌相关权重。使用多线程，提高脚本的运行速度。

## 模块安装

```python
pip install requests
```

## 使用方法

```python
python3 domain_check.py txt文件路径
```

![image-20240604182047570](https://foreverwlwl.oss-cn-beijing.aliyuncs.com/typora/202406041820646.png)

结果会输出到当前目录下的out文件夹内，结果文件命名根据时间命名，更好的判断出文件位置。

![image-20240604182152604](https://foreverwlwl.oss-cn-beijing.aliyuncs.com/typora/202406041821635.png)

![image-20240604182212796](https://foreverwlwl.oss-cn-beijing.aliyuncs.com/typora/202406041822837.png)

## 注意事项

尽量使用python3.9以上版本运行。有关脚本问题以及src挖掘交流联系email：168@foreverwl.top

