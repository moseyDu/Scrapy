爬虫框架
Scrapy教程：http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html


创建项目Scrapy，cmd中运行命令：scrapy startproject tutorial,该命令创建包含下列内容的tutorial目录：
    --scrapy.cfg:该项目的配置文件
    --tutorial/:该项目的Python模块
    --tutorial/items.py:项目中的item文件
    --tutorial/pipelines.py:项目中的pipelines文件
    --tutorial/settings.py:项目的设置文件
    --tutorial/spiders/:放置spider代码的目录


步骤：
一、在items.py定义一下字段；Item是保存爬取到的数据的容器，使用方法与Python字典类似
二、在spiders文件夹中编写自己的爬虫
三、在pipelines.py中存储自己的数据(如果文件很简单，可直接使用命令scrapy crawl qidian -o qidian.csv进行保存)



从网页中提取数据的方法，可使用XPath或css；
XPath表达式及其对应含义：
    /html/head/title:选择html文档中<head>标签内的title元素
    /html/head/title/text():选择上面提到的<title>元素的文字
    //td:选择所有的<td>元素
    //div[@class="mine"]:选择所有具有class="mine"属性的div元素





