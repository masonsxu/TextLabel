# TextLabel——数据标注系统
一款数据标注工具（仿照百度在线标注平台）

## 数据标注界面

数据标注界面主要分为4个板块：

1. 注明标注规范；

2. 各个按钮的功能介绍：

3. | 按钮名称         | 功能                                                         |
   | ---------------- | ------------------------------------------------------------ |
   | 开始标注         | 从数据库中读取未标注数据进行标注                             |
   | 撤回             | 删除上一步的标注错误                                         |
   | 下一篇           | 保存当前已经标注好的数据，并读取新的未标注数据               |
   | 退出当前文本标注 | 退出当前未完成标注，或者退出此次标注，退出后不能保存未完成标注，未完成标注会被重置成为未标注状态 |

   显示当前选中的文字与被标注的标记

4. 数据标注的工作区：

   1. 显示被读取的文本数据；
   2. 按住鼠标左键选中文本，在弹出的标记中选中应该被标注的标记

   

![image-20210317172225122](https://gitee.com/MasonsXu/cloudimg/raw/master/img/image-20210317172225122.png)

## 新建数据标注表（避免修改初始表）

将初始表中的数据进行去重处理后插入新建的数据标注表中：

```sql
INSERT INTO `TextLabel_schema`.`labelData`(`media_id`, `abstract`) SELECT ANY_VALUE(media_id),abstract FROM textLabel GROUP BY abstract;
```

初始表：

![image-20210317173555598](https://gitee.com/MasonsXu/cloudimg/raw/master/img/image-20210317173555598.png)

标注表：

![image-20210317173649512](https://gitee.com/MasonsXu/cloudimg/raw/master/img/image-20210317173649512.png)

## 代码目录介绍

```
TextLabel
	config
		config.cfg	# 数据库配置文件
		textLabel.sql	# 数据库初始表的建表语句
	create_database	
		run_sql.py	# 运行sql语句，简历初始表
	merge_text
		merge_text.py	# 将csv格式数据导入mysql数据库中
	models
		TextLabel_schema.py	# falsk_sqlalchemy链接数据库需要使用的各个表生成的models.py文件
	static	# 前端界面使用Vue3完成，并将生成的各个文件放到相应的位置
		css/
		fonts/
		js/
		favicon.ico
	templates # 前端界面使用Vue3完成，并将生成的各个文件放到相应的位置
		index.html
	EkgApp.py # 项目启动程序
```



## ⚠️程序不能直接运行，相应的后端数据库文件没有上穿（未完待续）