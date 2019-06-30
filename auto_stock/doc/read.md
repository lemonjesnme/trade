
#打包exe命令
pyinstaller -D server.py

打包命令参数
-F 表示生成单个可执行文件

-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！

-p 表示你自己自定义需要加载的类路径，一般情况下用不到

-i 表示可执行文件的图标
#打包要注意的问题

pyinstaller -F server.py --hidden-import flask


