# Faceworks

一个基于CNN的颜值打分器


## 项目划分

项目划分为几个子项目：

+ `facespider` 在网络上爬取人像照片的爬虫机器人
+ `pre-processor` 旋转、裁剪、调色等预处理人像工具集合
+ `grader` 一个基于Web的交叉评分系统，获取人像评分的数据
+ `cnn` 卷积神经网络设计、训练相关代码
+ `services` 对外提供服务的Web接口
