#encoding='UTF-8' 
from selenium import webdriver
import time
import os
import re
from bs4 import BeautifulSoup  #executable_path为chromedriver.exe的解压安装目录，需要与chrome浏览器同一文件夹下
import csv
option = webdriver.ChromeOptions()
driver=webdriver.Chrome(executable_path="C:\\Users\\user27\\Desktop\\chromedriver.exe")
url='https://www.icourse163.org/course/RUC-488001'#大学计算机
#url='https://www.icourse163.org/course/HZAU-1002731009'#C++语言程序设计
#url='https://www.icourse163.org/course/HZAU-1002739008'#数据结构
#url='https://www.icourse163.org/course/FJNU-1002582006' #网络安全与应用
#url='https://www.icourse163.org/course/NJTU-1001691004' #大学计算机——计算思维之路CAP
#url='https://www.icourse163.org/course/CUG-1003556007'   #爬取机器学习

driver.get(url)
cont=driver.page_source             #获得初始页面代码，接下来进行简单的解析
soup=BeautifulSoup(cont,'html.parser')
#print(soup)
ele=driver.find_element_by_id("review-tag-button")  #模仿浏览器就行点击查看课程评价的功能
ele.click()                      #上边的id，下边的classname都可以在源码中看到（首选火狐，谷歌）
xyy=driver.find_element_by_class_name("ux-pager_btn__next")#翻页功能，类名不能有空格，有空格可取后边的部分
connt=driver.page_source
soup=BeautifulSoup(connt,'html.parser')
#print(soup)
acontent=[]         #n页的总评论
content=soup.find_all('div',{'class':'ux-mooc-comment-course-comment_comment-list_item_body_content'})#包含全部评论项目的总表标签
#print(content)
for ctt in content:       #第一页评论的爬取
    scontent=[]
    aspan=ctt.find_all('span') #刚获得一页中的content中每一项评论还有少量标签
    for span in aspan:
        scontent.append(span.string)#只要span标签里边的评论内容
    acontent.append(scontent) #将一页中的一条评论加到总评论列表里，知道该页加完

print(acontent)
print(len(acontent))
for i in range(55): #翻页 286-0+1次，也就是287次，第一页打开就是，上边读完第一页了
    xyy.click()
    time.sleep(1)
    connt = driver.page_source
    soup = BeautifulSoup(connt,'html.parser')
    content = soup.find_all('div',{'class': 'ux-mooc-comment-course-comment_comment-list_item_body_content'})  # 包含全部评论项目的总表标签
    for ctt in content:
        scontent = []
        aspan = ctt.find_all('span')
        for span in aspan:
            scontent.append(span.string)
        acontent.append(scontent)
    print(acontent)
    with open("D:\\Github\\Chinese-corpus-sentiment-data-analysis\\1.csv", "w", newline="",encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(acontent)

