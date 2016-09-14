-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: pythonbeltexam
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pokes`
--

DROP TABLE IF EXISTS `pokes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pokes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `pokers_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pokes_users_idx` (`user_id`),
  KEY `fk_pokes_users1_idx` (`pokers_id`),
  CONSTRAINT `fk_pokes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_pokes_users1` FOREIGN KEY (`pokers_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokes`
--

LOCK TABLES `pokes` WRITE;
/*!40000 ALTER TABLE `pokes` DISABLE KEYS */;
INSERT INTO `pokes` VALUES (1,2,1,'2016-06-24 11:12:56','2016-06-24 11:12:56'),(2,2,1,'2016-06-24 11:12:58','2016-06-24 11:12:58'),(3,2,3,'2016-06-24 11:15:32','2016-06-24 11:15:32'),(4,2,3,'2016-06-24 11:15:33','2016-06-24 11:15:33'),(5,2,3,'2016-06-24 11:15:33','2016-06-24 11:15:33'),(6,2,3,'2016-06-24 11:15:34','2016-06-24 11:15:34'),(7,2,3,'2016-06-24 11:15:35','2016-06-24 11:15:35'),(8,2,1,'2016-06-24 11:30:08','2016-06-24 11:30:08'),(9,2,1,'2016-06-24 11:30:08','2016-06-24 11:30:08'),(10,3,1,'2016-06-24 11:30:10','2016-06-24 11:30:10'),(11,3,1,'2016-06-24 11:30:10','2016-06-24 11:30:10'),(12,4,1,'2016-06-24 11:48:59','2016-06-24 11:48:59'),(13,4,1,'2016-06-24 11:49:00','2016-06-24 11:49:00'),(14,4,1,'2016-06-24 11:49:00','2016-06-24 11:49:00'),(15,5,1,'2016-06-24 12:01:42','2016-06-24 12:01:42'),(16,3,1,'2016-06-24 12:02:58','2016-06-24 12:02:58'),(17,2,1,'2016-06-24 12:02:59','2016-06-24 12:02:59'),(18,1,2,'2016-06-24 12:03:32','2016-06-24 12:03:32'),(19,1,2,'2016-06-24 12:08:08','2016-06-24 12:08:08'),(20,1,5,'2016-06-24 12:08:19','2016-06-24 12:08:19'),(21,1,2,'2016-06-24 12:08:49','2016-06-24 12:08:49'),(22,1,2,'2016-06-24 12:08:50','2016-06-24 12:08:50'),(23,1,2,'2016-06-24 12:08:50','2016-06-24 12:08:50'),(24,6,1,'2016-06-24 12:43:55','2016-06-24 12:43:55');
/*!40000 ALTER TABLE `pokes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `dateofbirth` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'JDPenuliar','JD','jaydz.penuliar@gmail.com','$2b$12$YdYDH/3t/Y/uPtPfGmrmSOIZ.rm0P3gtm6SAfD3cpWROurXeggoD6','1995-05-18 00:00:00','2016-06-24 10:09:28','2016-06-24 10:09:28'),(2,'DonnPenuliar','Donn','donn.penuliar@gmail.com','$2b$12$rGOdUtLebV/3dw/Fe/KeV./gvjV7vbmw5mnOTJNWbpDzcRRKvGXrC','1995-05-18 00:00:00','2016-06-24 10:22:57','2016-06-24 10:22:57'),(3,'Joseph','Joseph','joseph@joseph.com','$2b$12$599ToOMV76ycqsa4ZbLF6egruz5q0Zzb60KoueLdMF1RZRNzaxpiu','2016-12-31 00:00:00','2016-06-24 11:15:28','2016-06-24 11:15:28'),(4,'haha','haha','haha@haha.com','$2b$12$29txToY8ZdoCsOrSHRW8YOH2zIquaVYQwHVbeihwznvTkLwz8suIa','2016-12-31 00:00:00','2016-06-24 11:33:05','2016-06-24 11:33:05'),(5,'zxcvzxcv','zxcv','z@z.com','$2b$12$RgHJG/xrmMGlse94H58qqOjws1D5Ro3i8/auuAey7Q6gpQWatSLl2','2016-12-31 00:00:00','2016-06-24 11:58:16','2016-06-24 11:58:16'),(6,'JDII','JDII','jdpenuliar@codingdojo.com','$2b$12$5cvUjxoPCAnr190e7FCyHOuJefeuPmffCKzwfdDsM1AP5k/6xlXhG','2016-12-31 00:00:00','2016-06-24 12:34:00','2016-06-24 12:34:00'),(7,'asdf','asdf','asdf@asdf.com','$2b$12$gHHhg94LGHWE5bjnpEifdOdpVyRsJKQv7M0xJb1iaroH7O1ZiRvFC','2016-12-31 00:00:00','2016-06-24 12:38:25','2016-06-24 12:38:25'),(8,'donnII','donII','haha2@haha.com','$2b$12$bT5v78izXaUTDzqaZga5Iu/uXDTtMNt1o.tgbpSoj5HFnQhWHErCa','2016-12-31 00:00:00','2016-06-24 12:45:22','2016-06-24 12:45:22'),(9,'danilo','danilo','danilo.penuliar@gmail.com','$2b$12$eThFr8uUxgVBKhpLDM8AfuM0dFvzGJ7bNwHo9VLjaXRnCtXx2lImW','2016-12-31 00:00:00','2016-06-24 12:48:14','2016-06-24 12:48:14'),(10,'hahaIV','haha5','haha5@haha.com','$2b$12$fQWZUZT35CAVVGPKefU6B.SNmf8O8HvHct/WGs3RaovwH7VmjRY3.','2016-12-31 00:00:00','2016-06-24 12:49:00','2016-06-24 12:49:00'),(11,'JDX','JDX','jdx@jdx.com','$2b$12$eMcOWk/cBSMu3iQdYKTEQOf95b8ILXyXobfbk94DBQ2vtzFKUmQ9y','2016-12-31 00:00:00','2016-06-24 12:49:25','2016-06-24 12:49:25');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-24 12:50:18
