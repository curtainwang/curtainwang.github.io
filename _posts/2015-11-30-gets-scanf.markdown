---
layout: post
title: gets和scanf   
category : C/C++
tagline: "C/C++"
tags : [C/C++]
---


gets和scanf函数的区别


##### 之前一直在用这两个函数，但是一直分不清有什么区别，有时候这个函数正常了另一个不正常，有时候有貌似都可以，在此也趁着十一月的最后一天的晚上，写篇博客:)
scanf()函数和gets()函数都可用于输入字符串，但在功能上有区别。
若想从键盘上输入字符串"hi hello"，则应该使用__gets__函数。

##### gets可以接收空格；

##### 而scanf遇到空格、回车和Tab键都会认为输入结束，所有它不能接收空格。

<pre>
char string[15]; 
gets(string); /*遇到回车认为输入结束*/
scanf("%s",string); /*遇到空格认为输入结束*/
</pre>

### 在输入的字符串中包含空格时，应该使用gets输入。

##### scanf和gets获取字符串时的区别(在C语言中，能构获取字符串的函数至少有两个)

### 1.scanf()
所在头文件：stdio.h

语法：scanf("格式控制字符串",变量地址列表);

接受字符串时：scanf("%s",字符数组名或指针);

### 2.gets()
所在头文件：stdio.h

语法：gets(字符数组名或指针);


 
#### 两者在接受字符串时：

#### 1.不同点：

scanf不能接受空格、制表符Tab、回车等；

而gets能够接受空格、制表符Tab和回车等；

#### 2.相同点：
字符串接受结束后自动加'\0'。

#### 例1：
#include stdio.h

void main()

{

	char ch1[10],ch2[10];

	scanf("%s",ch1);

	gets(ch2);

	return;

}

依次键入asd空格fg回车，asd空格fg回车，则ch1="asd\0"，ch2="asd fg\0"。



#### 例2：
#include stdio.h

void main()

{

	char ch1[10],ch2[10],c1,c2;

	scanf("%s",ch1);

	c1 = getchar();

	gets(ch2);

	c2 = getchar();

}

依次键入asdfg回车，asdfg回车，则ch1="asdfg\0"，c1='\n'，ch2="asdfg\0"，c2需输入。


#### scanf ：

#### 当遇到回车，空格和tab键会自动在字符串后面添加'\0'，但是回车，空格和tab键仍会留在输入的缓冲区中。scanf()可以读取所有类型的变量

##### gets：

##### 可接受回车键之前输入的所有字符，并用'\n'替代 '\0'.回车键不会留在输入缓冲区中

##### gets()用到读取字符串，用回车结束输入 


---