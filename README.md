#个人博客

**before**  
可以看看以前的博客，用的jekyll或者是hexo，强迫症找不到满意的主题，又不想动手做:)   

**2016-11-06 16:36**  
想弄成js自动加载文件夹下的所有文件，自动形成index主页，然而发现，ActiveXObject这个对象只有IE浏览器有，那么问题就来了，chrome、safari怎么办....  
真是输了:(


**2016-11-06 22:09**  
试试这个吧： http://www.w3school.com.cn/tiy/t.asp?f=xdom_httprequest_js_4   
1.写个bat脚本读取目录下的所有文件；  
2.生成一个file.txt的文本文件，里面列出所有文件名；  
3.然后根据上面的链接，后台请求这个file.txt文件，根据里面每一行的文件，动态生成每个li标签；  
4.其他一些方案：  
> https://imququ.com/post/a-downloader-with-filesystem-api.html
> https://www.html5rocks.com/zh/tutorials/file/filesystem/


**2016-11-20 20:31**
完成了个小的demo，对于python中的引号问题： 
1.带双引号的字符串用单引号括起来，带单引号的字符串用双引号括起来，两种都有的用/转义 
2.这个问题本来没什么的，但是在git的提交命令里，如果-m跟的备注信息是单引号，那么单引号里就不能有空格，只有跟双引号，才能有空格 
3.把本来的commit.bat里的内容整合进python脚本里了，方便提交了 
4.附commit.bat 
> git add .
> set tmp=%date:~0,10% %time:~0,8%
> git commit -m "%tmp%"
> git push


