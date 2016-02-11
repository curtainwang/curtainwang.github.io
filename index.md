---
layout: page
title: 部落
tagline: 嗯,人艰不拆...
---
{% include JB/setup %}

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

--------------------






####写在前面


Github上也是搭了又删，删了又搭，最后还是搞个简易点的吧，用Jekyll Bootstrap默认主题稍微有个布局。以后还是把重点放在内容上吧，记录一些一个学生菜鸟的学习备忘。

> Email: curtainwang@qq.com  