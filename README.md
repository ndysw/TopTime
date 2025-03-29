# TopTime
A simple app show current time on the top.
这是一个屏幕上显示当前时间的小程序，使用Python编制
pyinstaller --onefile --windowed time_display.py 封装成windows下可以运行的EXE文件
首次尝试上传github

备忘：本地项目上传步骤
1、在用户github上建立一个库:TopTime，其他步骤略
2、在准备上传的项目文件夹单击鼠标右键-更多选项-open git bash here,
输入： git init   初始化， 生成一个.git隐藏文件夹，显示全部隐藏文件夹可见
3、输入：git add .   回车
4、输入 git commit -m "first commit"   回车，发现如下错误：Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'ADMIN@TP-X230.(none)')

5、进入.git目录，使用VS CODE编辑config文件，增加下列内容
[user]
email=ndysw@126.com  （github注册用邮箱）
name=ndysw （github 用户名）
编辑完毕保存

6、重新执行  git commit -m "first commit"
待上传的文件全部显示出来

7、输入：git remote add TopTime（预备上传的github仓库名） https://github.com/ndysw/TopTime.git（仓库的code地址）  回车
8、输入：git push -u TopTime master   回车，等待文件上传
9、去github仓库查看上传文件

(备注：步骤8 将文件上传到master分支，默认分支为main，readme文档也在main分支，初次上传，小失误)

20250329:windows7可能提示缺少相关dll文件，可能提示缺少相关python组件，待修复
