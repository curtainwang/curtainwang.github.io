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


**2016-11-20 21:56**   
完成了个小的demo，对于python中的引号问题：  
1.带双引号的字符串用单引号括起来，带单引号的字符串用双引号括起来，两种都有的用/转义  
2.这个问题本来没什么的，但是在git的提交命令里，如果-m跟的备注信息是单引号，那么单引号里就不能有空格，只有跟双引号，才能有空格  
3.把本来的commit.bat里的内容整合进python脚本里了，方便提交了  
4.关于python的汉字编码问题，真是操碎了心，找了半天，试了各种方法，才发现是Windows系统返回的是gb2312的编码的字符串，需要解码：参考链接[http://xanderzhang.iteye.com/blog/465992]
> 首先要搞清楚，字符串在Python内部的表示是unicode编码. 因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。   
> (1) decode的作用是将其他编码的字符串转换成unicode编码， 如str1.decode('gb2312')，表示将gb2312编码的字符串转换成unicode编码。  
> (2) encode的作用是将unicode编码转换成其他编码的字符串， 如str2.encode('gb2312')，表示将unicode编码的字符串转换成gb2312编码。   
>  (3)在某些IDE中，字符串的输出总是出现乱码，甚至错误，其实是由于IDE的结果输出控制台自身不能显示字符串的编码，而不是程序本身的问题     


5.附commit.bat   
> git add .  
> set tmp=%date:~0,10% %time:~0,8%  
> git commit -m "%tmp%"  
> git push  


