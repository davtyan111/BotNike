-- MySQL dump 10.13  Distrib 8.0.42, for Linux (x86_64)
--
-- Host: localhost    Database: photo_bot_db
-- ------------------------------------------------------
-- Server version	8.0.42-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (19,'2');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tariff` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `subcode` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'1308580836','2','glo','kentron','2025-06-21 12:11:22'),(2,'1308580836','2','glo','kentron','2025-06-21 12:17:12'),(3,'1308580836','2','glo','kentron','2025-06-21 12:24:45'),(4,'1308580836','2','glo','kentron','2025-06-21 12:33:34'),(5,'1308580836','2','glo','kentron','2025-06-21 14:09:50'),(6,'1308580836','2','glo','kentron','2025-06-21 14:11:28'),(7,'1308580836','1','moonrock','masiv','2025-06-21 14:14:28'),(8,'1308580836','1','kotlet','masiv','2025-06-21 14:56:22'),(9,'949702991','1','yad','kentron','2025-06-21 15:33:56'),(10,'949702991','2','kotlet','kentron','2025-06-21 15:34:52'),(11,'7043538167','aa','dd','ss','2025-06-21 19:43:51'),(12,'7043538167','aa','dd','ss','2025-06-21 19:44:35'),(13,'7043538167','aa','dd','ss','2025-06-21 19:54:51'),(14,'7043538167','aa','dd','ss','2025-06-21 20:03:18'),(15,'7043538167','ss','dd','ds','2025-06-21 20:04:23'),(16,'7043538167','aa','asa','ds','2025-06-21 20:04:45'),(17,'7043538167','a','c','ds','2025-06-21 20:05:57'),(18,'1308580836','a','c','ds','2025-06-21 21:17:28'),(19,'1308580836','aa','dd','ss','2025-06-21 21:18:32'),(20,'1308580836','aa','dd','ss','2025-06-21 21:19:47'),(21,'1308580836','1','3','2','2025-06-21 21:27:09'),(22,'1308580836','4','6','5','2025-06-21 21:32:21'),(23,'1308580836','8','9','7','2025-06-21 21:42:30'),(24,'1308580836','1','3','2','2025-06-21 21:48:59'),(25,'1308580836','11','33','22','2025-06-21 21:50:24'),(26,'1308580836','1','3','2','2025-06-21 21:53:47'),(27,'1308580836','8','9','7','2025-06-21 21:54:36'),(28,'7043538167','8','6','7','2025-06-21 21:58:03'),(29,'7043538167','11','33','22','2025-06-21 21:58:18'),(30,'1308580836','11','33','22','2025-06-21 22:02:08'),(31,'7043538167','1','3','2','2025-06-21 22:05:35'),(32,'1308580836','1','3','22','2025-06-21 22:06:25'),(33,'1308580836','1','3','2','2025-06-21 22:06:36'),(34,'1308580836','1','3','2','2025-06-21 22:07:00'),(35,'1308580836','4','3','5','2025-06-22 09:02:13'),(36,'1308580836','8','9','7','2025-06-22 09:02:41'),(37,'1308580836','8','9','7','2025-06-22 10:32:23'),(38,'1308580836','1','glo','sevan','2025-08-16 16:13:47'),(39,'1308580836','1','1','1','2025-08-16 16:34:16'),(40,'1308580836','1','1','1','2025-08-16 17:32:25'),(41,'1308580836','1','1','1','2025-08-16 17:47:25'),(42,'1308580836','qw','qw','qw','2025-08-16 18:26:24'),(43,'1308580836','1','1','1','2025-08-16 18:26:38'),(44,'1308580836','qw','qw','qw','2025-08-16 18:27:31'),(45,'1308580836','rr','rr','rr','2025-08-16 18:28:52'),(46,'1308580836','1','3','2','2025-08-16 18:50:12'),(47,'1308580836','1','3','2','2025-08-16 19:13:11'),(48,'1308580836','1','3','2','2025-08-16 19:13:21');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'pending',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photos`
--

DROP TABLE IF EXISTS `photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `drive_file_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tariff` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `subcode` varchar(160) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` varchar(160) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photos`
--

LOCK TABLES `photos` WRITE;
/*!40000 ALTER TABLE `photos` DISABLE KEYS */;
INSERT INTO `photos` VALUES (1,'12gNMhnPDV7-MBScTBB1bovedSfaFS6Hu','0.5','glo','kentron','2025-06-20 15:49:35',NULL,NULL),(2,'1JGQzlLpG1TkrlC5vAqKvALL6rVnJgXDo','0.5','glo','kentron','2025-06-20 17:39:02',NULL,NULL),(3,'1wsIXn6pBQMAZ3Ox4MeH1D_wcnzdxvdEk','2','glo','kentron','2025-06-20 21:20:48',NULL,NULL),(4,'1rbRN6IphBVKUUY1GRhbrMsbjgXLk5bVW','2','glo','kentron','2025-06-20 22:38:22',NULL,NULL),(5,'17wBywL4CcIDD2haNPzqHersVYhxNL9Mw','1','moonrock','masiv ','2025-06-21 14:14:06',NULL,NULL),(6,'1OoW5tnIjlyQLTyEBpdGVTxvupemw4A8c','1','kotlet','masiv ','2025-06-21 14:55:57',NULL,NULL),(7,'13pyx7NWaxTbOaHig6Y-2ljHLyN7l6kjk','3','yad','kentron','2025-06-21 15:32:42',NULL,NULL),(8,'1rEhd2jeSRj0kIpHs14_6DiQNnskqmbB4','2','kotlet','kentron','2025-06-21 15:34:19',NULL,NULL),(9,'1zE2WsVx3pqT5gANBvIKWMMUp0gXh3t6N','aa','dd','ss','2025-06-21 19:43:28','127.0.0.1',NULL),(10,'1R0yWFwyeBxn3qtHUaP4u7YTAyvhy-4mm','aa','dd','ds','2025-06-21 20:04:10',NULL,NULL),(11,'129CGTtAhtthdwlqvGNoLF05iuVFgGpjJ','a','c','ds','2025-06-21 20:05:21',NULL,NULL),(12,'1zVdisIIjRZoupdXwwuh74DbB5bUg20pY','aa','dd','ss','2025-06-21 21:18:11',NULL,NULL),(13,'1Y2fFrWIcyvNMvc4bsoTbzO6OIceBQ1qG','1','3','2','2025-06-21 21:21:36',NULL,NULL),(14,'1GECwcxa7--FgDFjSKbB1bVIxnePGm6ru','4','6','5','2025-06-21 21:31:49',NULL,NULL),(15,'1266EWWp5YOFSyGl2VWsdlQs23BKMgyyM','8','9','7','2025-06-21 21:41:29','',NULL),(16,'1MZ0oHtOZsYLjYtcXc5pvgMHaNFA53wxX','11','33','22','2025-06-21 21:49:56','',NULL),(17,'1266EWWp5YOFSyGl2VWsdlQs23BKMgyyM','8','9','7','2025-06-21 21:54:36','1308580836',NULL),(18,'1MZ0oHtOZsYLjYtcXc5pvgMHaNFA53wxX','11','33','22','2025-06-21 21:58:18','7043538167',NULL),(19,'1MZ0oHtOZsYLjYtcXc5pvgMHaNFA53wxX','11','33','22','2025-06-21 22:02:08','1308580836',NULL),(20,'1Y2fFrWIcyvNMvc4bsoTbzO6OIceBQ1qG','1','3','2','2025-06-21 22:05:35','7043538167',NULL),(21,'1Y2fFrWIcyvNMvc4bsoTbzO6OIceBQ1qG','1','3','2','2025-06-21 22:06:36','1308580836',NULL),(22,'1Y2fFrWIcyvNMvc4bsoTbzO6OIceBQ1qG','1','3','2','2025-06-21 22:07:00','1308580836',NULL),(23,'1266EWWp5YOFSyGl2VWsdlQs23BKMgyyM','8','9','7','2025-06-22 09:02:42','1308580836',NULL),(24,'1266EWWp5YOFSyGl2VWsdlQs23BKMgyyM','8','9','7','2025-06-22 10:32:24','1308580836',NULL),(26,'15bL-kWGcQzXLBLMptSs9jhLCYax9-j0s','qw','qw','qw','2025-06-22 10:59:32','',''),(27,'1vGQFAaSW7p-T-Y1GR4LotkQn2eDFCenA','qw','qw','qw','2025-06-22 10:59:50','',''),(28,'1aqi_H7R6Safgz-g1IRMQBWTgImRRhNKz','1','1','1','2025-08-16 17:27:18',NULL,NULL),(29,'1DNkJhtPolBpTKqJf7cWu0-AMRaCeR4Sk','qw','qw','qw','2025-08-16 18:25:31',NULL,NULL),(30,'1nLdNbvT-o9CWaU8XwecHg84a9xS73RQ-','qw','qw','qw','2025-08-16 18:26:58',NULL,NULL),(31,'1DdqPC6lV3vLkBf7RzgVhgSJ90rO2mKxL','rr','rr','rr','2025-08-16 18:28:24',NULL,NULL),(32,'1ELqJh9bAQTzrYwqZ6YYii8qUHMcXal7G','1','3','2','2025-08-16 18:50:00',NULL,NULL),(33,'12RTKAihnlNMYRrQw7lWYW_Gi5SZxwv4S','1','3','2','2025-08-16 19:12:58',NULL,NULL);
/*!40000 ALTER TABLE `photos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcodes`
--

DROP TABLE IF EXISTS `subcodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subcodes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcodes`
--

LOCK TABLES `subcodes` WRITE;
/*!40000 ALTER TABLE `subcodes` DISABLE KEYS */;
INSERT INTO `subcodes` VALUES (18,'3');
/*!40000 ALTER TABLE `subcodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tariffs`
--

DROP TABLE IF EXISTS `tariffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tariffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price_dash` decimal(10,4) DEFAULT '0.0500',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tariffs`
--

LOCK TABLES `tariffs` WRITE;
/*!40000 ALTER TABLE `tariffs` DISABLE KEYS */;
INSERT INTO `tariffs` VALUES (35,'1',0.0500);
/*!40000 ALTER TABLE `tariffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `balance` decimal(18,8) DEFAULT '0.00000000',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
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

-- Dump completed on 2025-08-17 21:35:34
