CREATE TABLE `t_storage` (
                             `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
                             `title` varchar(255) DEFAULT NULL,
                             `original_text` text COMMENT '原文',
                             `modify_text` text COMMENT '修改过的内容',
                             `translation_text` text COMMENT '译文',
                             `translation_title` text COMMENT '标题译文',
                             `released` int(1) DEFAULT '0' COMMENT '是否已发布',
                             `replaced` int(1) DEFAULT '0' COMMENT '0未进行替换1已替换',
                             `extracted` int(1) DEFAULT '0' COMMENT '是否已提取人名或地名',
                             `translated` int(1) DEFAULT '0' COMMENT '是否已翻译',
                             `chapter_number` int(8) DEFAULT '0' COMMENT '章节序号',
                             PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `t_replace` (
                             `id` int(11) NOT NULL AUTO_INCREMENT,
                             `type` int(11) DEFAULT NULL COMMENT '0:姓名1地址',
                             `original_text` varchar(255) DEFAULT NULL,
                             `new_text` varchar(255) DEFAULT NULL,
                             `del_flag` int(11) DEFAULT '0',
                             PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
