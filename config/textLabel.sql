/*
 Navicat Premium Data Transfer

 Source Server         : masonsxu
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : TextLabel_schema

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 08/02/2021 19:33:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for textLabel
-- ----------------------------
DROP TABLE IF EXISTS `textLabel`;
CREATE TABLE `textLabel` (
  `media_id` int NOT NULL AUTO_INCREMENT COMMENT '新闻序号',
  `media_type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '媒体类型',
  `media_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '媒体名称',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '标题',
  `abstract` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT '摘要',
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '作者',
  `number_of_similar_articles` int DEFAULT NULL COMMENT '相似文章条数',
  `original_link` varchar(2083) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '原文链接',
  `keyword_frequency` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '关键词频率',
  `whether_the_keyword_appears_in_the_title` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '关键词标题中出现与否',
  `topic_term` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '主题词',
  `emotional_attribute` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '情感属性',
  `emotional_score` int DEFAULT NULL COMMENT '情感分值',
  `mention_region` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '提及地域',
  `release_time` varchar(255) DEFAULT NULL COMMENT '发布时间',
  `micro_Number_of_blog_fans` int DEFAULT NULL COMMENT '微博粉丝数',
  `number_of_reads` int DEFAULT NULL COMMENT '阅读数',
  `number_of_likes` int DEFAULT NULL COMMENT '点赞数',
  `original_author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '原作者',
  `number_of_comments` int DEFAULT NULL COMMENT '评论数',
  `number_of_reposts` int DEFAULT NULL COMMENT '转发数',
  PRIMARY KEY (`media_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
