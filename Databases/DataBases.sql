/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.33 : Database - bugs
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bugs` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bugs`;

/*Table structure for table `adminsapp_admins` */

DROP TABLE IF EXISTS `adminsapp_admins`;

CREATE TABLE `adminsapp_admins` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_admins` */

insert  into `adminsapp_admins`(`id`,`username`,`password`) values 
(1,'admin@gmail.com',12345);

/*Table structure for table `adminsapp_employee` */

DROP TABLE IF EXISTS `adminsapp_employee`;

CREATE TABLE `adminsapp_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `empid` int NOT NULL,
  `empname` varchar(100) NOT NULL,
  `job` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `dateofjoin` date NOT NULL,
  `salary` int NOT NULL,
  `gender` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_employee` */

insert  into `adminsapp_employee`(`id`,`empid`,`empname`,`job`,`email`,`password`,`dateofjoin`,`salary`,`gender`,`role`) values 
(1,1,'employee1','manager','manager@gmail.com','12345','2024-05-20',25000,'male','tester'),
(2,2,'employee2','devolper','devolper@gmail.com','12345','2024-05-21',30000,'male','devloper'),
(3,3,'employee3','manager','analyst@gmail.com','12345','2024-05-16',50000,'male','analyst'),
(4,4,'employee4','manager','tester@gmail.com','12345','2024-05-29',80000,'male','manager');

/*Table structure for table `adminsapp_news` */

DROP TABLE IF EXISTS `adminsapp_news`;

CREATE TABLE `adminsapp_news` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_news` */

/*Table structure for table `adminsapp_project` */

DROP TABLE IF EXISTS `adminsapp_project`;

CREATE TABLE `adminsapp_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `code` varchar(100) NOT NULL,
  `technology` varchar(100) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `manager` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `adminsapp_project` */

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add admins',7,'add_admins'),
(26,'Can change admins',7,'change_admins'),
(27,'Can delete admins',7,'delete_admins'),
(28,'Can view admins',7,'view_admins'),
(29,'Can add employee',8,'add_employee'),
(30,'Can change employee',8,'change_employee'),
(31,'Can delete employee',8,'delete_employee'),
(32,'Can view employee',8,'view_employee'),
(33,'Can add project',9,'add_project'),
(34,'Can change project',9,'change_project'),
(35,'Can delete project',9,'delete_project'),
(36,'Can view project',9,'view_project'),
(37,'Can add news',10,'add_news'),
(38,'Can change news',10,'change_news'),
(39,'Can delete news',10,'delete_news'),
(40,'Can view news',10,'view_news'),
(41,'Can add contact',11,'add_contact'),
(42,'Can change contact',11,'change_contact'),
(43,'Can delete contact',11,'delete_contact'),
(44,'Can view contact',11,'view_contact'),
(45,'Can add task',12,'add_task'),
(46,'Can change task',12,'change_task'),
(47,'Can delete task',12,'delete_task'),
(48,'Can view task',12,'view_task'),
(49,'Can add testcase',13,'add_testcase'),
(50,'Can change testcase',13,'change_testcase'),
(51,'Can delete testcase',13,'delete_testcase'),
(52,'Can view testcase',13,'view_testcase'),
(53,'Can add bug',14,'add_bug'),
(54,'Can change bug',14,'change_bug'),
(55,'Can delete bug',14,'delete_bug'),
(56,'Can view bug',14,'view_bug'),
(57,'Can add requirements',15,'add_requirements'),
(58,'Can change requirements',15,'change_requirements'),
(59,'Can delete requirements',15,'delete_requirements'),
(60,'Can view requirements',15,'view_requirements');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(7,'adminsapp','admins'),
(8,'adminsapp','employee'),
(10,'adminsapp','news'),
(9,'adminsapp','project'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(14,'employeeapp','bug'),
(15,'employeeapp','requirements'),
(13,'employeeapp','testcase'),
(11,'managementapp','contact'),
(12,'managementapp','task'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-05-25 08:07:42.001590'),
(2,'auth','0001_initial','2024-05-25 08:07:42.686868'),
(3,'admin','0001_initial','2024-05-25 08:07:42.828105'),
(4,'admin','0002_logentry_remove_auto_add','2024-05-25 08:07:42.834218'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-05-25 08:07:42.840017'),
(6,'adminsapp','0001_initial','2024-05-25 08:07:42.853520'),
(7,'adminsapp','0002_employee','2024-05-25 08:07:42.868253'),
(8,'adminsapp','0003_project','2024-05-25 08:07:42.881735'),
(9,'adminsapp','0004_news','2024-05-25 08:07:42.895617'),
(10,'contenttypes','0002_remove_content_type_name','2024-05-25 08:07:43.022744'),
(11,'auth','0002_alter_permission_name_max_length','2024-05-25 08:07:43.106673'),
(12,'auth','0003_alter_user_email_max_length','2024-05-25 08:07:43.131357'),
(13,'auth','0004_alter_user_username_opts','2024-05-25 08:07:43.137576'),
(14,'auth','0005_alter_user_last_login_null','2024-05-25 08:07:43.208712'),
(15,'auth','0006_require_contenttypes_0002','2024-05-25 08:07:43.210825'),
(16,'auth','0007_alter_validators_add_error_messages','2024-05-25 08:07:43.215686'),
(17,'auth','0008_alter_user_username_max_length','2024-05-25 08:07:43.288868'),
(18,'auth','0009_alter_user_last_name_max_length','2024-05-25 08:07:43.364368'),
(19,'auth','0010_alter_group_name_max_length','2024-05-25 08:07:43.377139'),
(20,'auth','0011_update_proxy_permissions','2024-05-25 08:07:43.383645'),
(21,'auth','0012_alter_user_first_name_max_length','2024-05-25 08:07:43.456700'),
(22,'employeeapp','0001_initial','2024-05-25 08:07:43.471661'),
(23,'employeeapp','0002_alter_testcase_date_of_creation','2024-05-25 08:07:43.496675'),
(24,'employeeapp','0003_auto_20211101_1254','2024-05-25 08:07:43.533052'),
(25,'employeeapp','0004_rename_severity_bug_sevearity','2024-05-25 08:07:43.551545'),
(26,'employeeapp','0005_auto_20211101_1624','2024-05-25 08:07:43.578139'),
(27,'employeeapp','0006_alter_bug_date','2024-05-25 08:07:43.600819'),
(28,'employeeapp','0007_status','2024-05-25 08:07:43.612010'),
(29,'employeeapp','0008_remove_status_bug_id','2024-05-25 08:07:43.619841'),
(30,'employeeapp','0009_delete_status','2024-05-25 08:07:43.627468'),
(31,'employeeapp','0010_requirements','2024-05-25 08:07:43.692619'),
(32,'employeeapp','0011_requirements_email','2024-05-25 08:07:43.708522'),
(33,'employeeapp','0012_testcase_requirements','2024-05-25 08:07:43.763319'),
(34,'employeeapp','0013_alter_testcase_requirements','2024-05-25 08:07:43.844236'),
(35,'managementapp','0001_initial','2024-05-25 08:07:43.855696'),
(36,'managementapp','0002_task','2024-05-25 08:07:43.867685'),
(37,'sessions','0001_initial','2024-05-25 08:07:43.889905');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('7ap7fzec1w9kvbv872hcoug27uy5ssh3','.eJyrVkrNTczMUbJSSsxLzKksLnFIB_H1kvNzlXSUivJzUhFSSrUAeS8QEg:1sBSdn:fOeDMNvZMmgguEl2E4KnF69yTretLI8ACBNL9EqEY6M','2024-06-10 05:11:23.920855'),
('klrphlbdg81d1b6uddkk6jmv2neuofgr','eyJlbWFpbCI6ImRldm9scGVyQGdtYWlsLmNvbSIsInJvbGUiOiJkZXZsb3BlciJ9:1sB7fm:Y8qkU1IhIcPiif8asenV0mQIMiT-EeePEHMEjjZ25SQ','2024-06-09 06:48:02.864833');

/*Table structure for table `employeeapp_bug` */

DROP TABLE IF EXISTS `employeeapp_bug`;

CREATE TABLE `employeeapp_bug` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `testcase_id` int NOT NULL,
  `description` varchar(350) NOT NULL,
  `test_path` varchar(300) NOT NULL,
  `screenshot` varchar(100) NOT NULL,
  `sevearity` varchar(300) NOT NULL,
  `priority` varchar(300) NOT NULL,
  `status` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `tested_by_email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_bug` */

/*Table structure for table `employeeapp_requirements` */

DROP TABLE IF EXISTS `employeeapp_requirements`;

CREATE TABLE `employeeapp_requirements` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(350) NOT NULL,
  `priority` varchar(300) NOT NULL,
  `ndatetime` datetime(6) NOT NULL,
  `projects_id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `employeeapp_requirem_projects_id_b41043d8_fk_adminsapp` (`projects_id`),
  CONSTRAINT `employeeapp_requirem_projects_id_b41043d8_fk_adminsapp` FOREIGN KEY (`projects_id`) REFERENCES `adminsapp_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_requirements` */

/*Table structure for table `employeeapp_testcase` */

DROP TABLE IF EXISTS `employeeapp_testcase`;

CREATE TABLE `employeeapp_testcase` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_name` varchar(350) NOT NULL,
  `module_name` varchar(350) NOT NULL,
  `senario` varchar(350) NOT NULL,
  `description` varchar(350) NOT NULL,
  `input_data` varchar(350) NOT NULL,
  `type_of_exception` varchar(350) NOT NULL,
  `pre_condition` varchar(350) NOT NULL,
  `expected_actual_result` varchar(350) NOT NULL,
  `status` varchar(300) NOT NULL,
  `date_of_creation` date NOT NULL,
  `tester_email` varchar(254) NOT NULL,
  `requirements` varchar(350) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `employeeapp_testcase` */

/*Table structure for table `managementapp_contact` */

DROP TABLE IF EXISTS `managementapp_contact`;

CREATE TABLE `managementapp_contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `managementapp_contact` */

/*Table structure for table `managementapp_task` */

DROP TABLE IF EXISTS `managementapp_task`;

CREATE TABLE `managementapp_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `manager_email` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `employee_email` varchar(254) NOT NULL,
  `project` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `enddate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `managementapp_task` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
