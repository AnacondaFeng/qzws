# qzws

## VSCode设置Git成功 2021.02.21 23:16 ,Next to upload github

# **基础资料**
1. 使用Anaconda+VSCode
2. 开发环境：Ubuntu20.04
3. 创建虚拟环境，安装指定版本Django命令 conda install django=version
4. VSCode设置默认python运行环境，Ctrl+Shift+P快捷键

# **开始创建Django后端程序**
1. 创建Project
django-admin.py startproject 项目名
2. 创建App
python manage.py startapp student
3. 把新创建的App都统一放到Apps的文件夹中
修改setting文件
import os,sys
sys.path.insert(0, os.path.join(BASE_DIR,'apps'))
4. 用ORM连接数据库
在Models文件创建对应类
5. 修改setting文件设置数据库连接
修改DATABASES
```python
‘default’:{
	'ENGINE':'django.db.backends.mysql',
	'NAME':'studentdb',
	'USER':'root',
	'PASSWORD':'qwer1234',
	'HOST':'localhost',
	'PORT':'3306',
}
```
6. 确保安装pymysql组件连接mysql数据库
使用conda install安装
7. app要加载pymysql
```python
app students文件中__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```
8. 建的类自动映射到库里的命令
```python
python manage.py makemigrations 生成执行脚本
python manage.py migrate 到数据库创建表
```

# **开始创建VUE前端**
1. VSCode安装扩展插件
```html
html格式化JS-CSS-HTML Formatter
vue插件Vue 3 Snippets
webServer插件Live Server
```
2. 使用element组件要注意的点
```html
必须要导入vue:	<script src="js/index.js"></script>
index.js要声明：
new Vue({
    el: '#app',
})
```
3. 安装chrome扩展工具用于调试vue  

# **VUE基础知识学习**#
1. 搭建环境使用CDN的方法
```html
<!-- 导入vue 开发版 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<!-- 导入element -->
<!-- 引入样式 -->
<link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
<!-- 引入组件库 -->
<script src="https://unpkg.com/element-ui/lib/index.js"></script>
```
2. 常用命令（去查官网KPI学习）
### **index01.html**
+ case01.双向数据绑定:v-model
+ case02.对数组/对象进行循环操作:v-for，:key指令绑定唯一key，重用元素提高效率

# 使用HBuilder X开发前端，测试Git用 20210226