/* Initdb */ 
CREATE DATABASE IF NOT EXISTS trace_db;

USE trace_db; 

/* Add more configuration and initial data below */
CREATE TABLE IF NOT EXISTS user_profile_data (
    `name` VARCHAR(48) CHARACTER SET utf8,
    `wxid` VARCHAR(48) CHARACTER SET utf8
);

CREATE TABLE IF NOT EXISTS trace_member_data (
    `name` VARCHAR(48) CHARACTER SET utf8,
    `uid` VARCHAR(48) CHARACTER SET utf8,
    `count` INT UNSIGNED
);

CREATE TABLE IF NOT EXISTS visit_data (
    `ip` VARCHAR(48) CHARACTER SET utf8, 
    `rec` VARCHAR(48) CHARACTER SET utf8, 
    `time` VARCHAR(48) CHARACTER SET utf8
); 

INSERT INTO user_profile_data VALUES 
    ('Test user 1', 'uu1'), ('Test user 2', 'uu2'); 

INSERT INTO trace_member_data VALUES 
    ('Adam Chen', "0", 0), 
    ('Ziqi Yan', "1", 0),
    ('Yichen Zhong', "2", 0),
    ('Tianye Song', "3", 0),
    ('Yexin Gao', "4", 0),
    ('Leo Hu', "5", 0),
    ('Boyang Wang', "6", 0),
    ('Chiev Wan', "7", 0),
    ('Mandy Luo', "8", 0),
    ('Yizhou Wang', "9", 0),
    ('Ruoqi Huang', "10", 0),
    ('Chuxuan Zheng', "11", 0),
    ('Dian Gao', "12", 0); 