# coding: utf-8
# 使用自动配置脚本生成的 flask_sqlalchemy models文件
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class LabelDatum(db.Model):
    __tablename__ = 'labelData'

    media_id = db.Column(db.Integer, primary_key=True, info='序号')
    abstract = db.Column(db.String, info='摘要')
    abstract_label = db.Column(db.String, info='标注后的摘要')
    label_flag = db.Column(db.String(10), info='标注状态')


class TextLabel(db.Model):
    __tablename__ = 'textLabel'

    media_id = db.Column(db.Integer, primary_key=True, info='新闻序号')
    media_type = db.Column(db.Text(collation='utf8mb4_0900_ai_ci'), info='媒体类型')
    media_name = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='媒体名称')
    title = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='标题')
    abstract = db.Column(db.String(collation='utf8mb4_0900_ai_ci'), info='摘要')
    author = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='作者')
    number_of_similar_articles = db.Column(db.Integer, info='相似文章条数')
    original_link = db.Column(db.String(2083, 'utf8mb4_0900_ai_ci'), info='原文链接')
    keyword_frequency = db.Column(db.String(14, 'utf8mb4_0900_ai_ci'), info='关键词频率')
    whether_the_keyword_appears_in_the_title = db.Column(
        db.String(2, 'utf8mb4_0900_ai_ci'), info='关键词标题中出现与否'
    )
    topic_term = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='主题词')
    emotional_attribute = db.Column(db.String(4, 'utf8mb4_0900_ai_ci'), info='情感属性')
    emotional_score = db.Column(db.Integer, info='情感分值')
    mention_region = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='提及地域')
    release_time = db.Column(db.String(255), info='发布时间')
    micro_Number_of_blog_fans = db.Column(db.Integer, info='微博粉丝数')
    number_of_reads = db.Column(db.Integer, info='阅读数')
    number_of_likes = db.Column(db.Integer, info='点赞数')
    original_author = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), info='原作者')
    number_of_comments = db.Column(db.Integer, info='评论数')
    number_of_reposts = db.Column(db.Integer, info='转发数')
