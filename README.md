# TextLabel——数据标注系统
一款数据标注工具（仿照百度在线标注平台）

## 新建数据标注专用的表

将初始表中的数据进行去重处理后插入新建的数据标注表中：

```sql
INSERT INTO `TextLabel_schema`.`labelData`(`media_id`, `abstract`) SELECT ANY_VALUE(media_id),abstract FROM textLabel GROUP BY abstract;
```

