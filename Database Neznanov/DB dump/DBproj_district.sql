-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: DBproj
-- ------------------------------------------------------
-- Server version	5.7.12

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
-- Table structure for table `district`
--

DROP TABLE IF EXISTS `district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` float unsigned DEFAULT NULL,
  `distName` varchar(50) NOT NULL,
  `population` float unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `district`
--

LOCK TABLES `district` WRITE;
/*!40000 ALTER TABLE `district` DISABLE KEYS */;
INSERT INTO `district` VALUES (1,5.29,'Алексеевский',78421),(2,3.25,'Алтуфьевский',55127),(3,2.11,'Арбат',28179),(4,4.58,'Аэропорт',73029),(5,5.07,'Бабушкинский',86210),(6,8.37,'Басманный',108204),(7,5.56,'Беговой',41505),(8,3.3,'Бескудниковский',73148),(9,6.45,'Бибирево',155599),(10,14.77,'Бирюлёво Восточное',145100),(11,8.51,'Бирюлёво Западное',85726),(12,10.24,'Богородское',104415),(13,7.63,'Братеево',102600),(14,5.04,'Бутырский',68654),(15,10.72,'Вешняки',118982),(16,17.42,'Внуково',21041),(17,6.61,'Войковский',64933),(18,3.77,'Восточное Дегунино',94565),(19,3.85,'Восточное Измайлово',76312),(20,3.14,'Восточный',12327),(21,14.97,'Выхино-Жулебино',219626),(22,5.5,'Гагаринский',76672),(23,8.93,'Головинский',100886),(24,14.99,'Гольяново',157040),(25,12.6,'Даниловский',91109),(26,7.29,'Дмитровский',87779),(27,5.73,'Донской',48441),(28,7.95,'Дорогомилово',67720),(29,4.32,'Замоскворечье',55612),(30,7.53,'Западное Дегунино',78811),(31,5.45,'Зюзино',123003),(32,4.38,'Зябликово',130229),(33,10.19,'Ивановское',122866),(34,15.24,'Измайлово',102837),(35,8.06,'Капотня',31168),(36,7.18,'Коньково',153272),(37,5.38,'Коптево',96992),(38,15.05,'Косино-Ухтомский',72144),(39,3.94,'Котловка',64317),(40,4.96,'Красносельский',47256),(41,12.04,'Крылатское',78509),(42,10.49,'Крюково',85219),(43,8.15,'Кузьминки',142249),(44,16.56,'Кунцево',142497),(45,7.9,'Куркино',21155),(46,8,'Левобережный',51457),(47,9.06,'Лефортово',90021),(48,5.79,'Лианозово',79582),(49,3.34,'Ломоносовский',84148),(50,5.54,'Лосиноостровский',80919),(51,17.41,'Люблино',165759),(52,2.97,'Марфино',26955),(53,4.68,'Марьина Роща',65973),(54,11.91,'Марьино',247479),(55,4.38,'Матушкино',38075),(56,27.57,'Метрогородок',36154),(57,4.6,'Мещанский',58002),(58,12.67,'Митино',178518),(59,10.73,'Можайский',132373),(60,26.25,'Молжаниновский',3521),(61,9.3,'Москворечье-Сабурово',76162),(62,8.17,'Нагатино-Садовники',76284),(63,9.8,'Нагатинский Затон',115354),(64,5.42,'Нагорный',77878),(65,5.58,'Некрасовка',19940),(66,7.57,'Нижегородский',43799),(67,4.45,'Новогиреево',94562),(68,3.6,'Новокосино',103765),(69,8.48,'Ново-Переделкино',111047),(70,6.11,'Обручевский',78619),(71,7.67,'Орехово-Борисово Северное',129221),(72,6.94,'Орехово-Борисово Южное',145588),(73,12.46,'Останкинский',61407),(74,10.18,'Отрадное',175537),(75,17.54,'Очаково-Матвеевское',118891),(76,9.73,'Перово',139351),(77,17.89,'Печатники',83403),(78,12.9,'Покровское-Стрешнево',53786),(79,5.61,'Преображенское',83507),(80,11.7,'Пресненский',123284),(81,4.65,'Проспект Вернадского',61045),(82,18.54,'Раменки',125128),(83,3.54,'Ростокино',37505),(84,6.49,'Рязанский',101982),(85,8.13,'Савёлки',32074),(86,2.7,'Савёловский',57998),(87,4.41,'Свиблово',60323),(88,9.13,'Северное Бутово',90116),(89,4.2,'Северное Измайлово',85094),(90,5.66,'Северное Медведково',123073),(91,9.4,'Северное Тушино',156381),(92,10.29,'Северный',27992),(93,10.4,'Силино',37807),(94,3.72,'Сокол',57133),(95,7.84,'Соколиная Гора',85959),(96,10.28,'Сокольники',57444),(97,11.29,'Солнцево',113959),(98,3.81,'Старое Крюково',28537),(99,16.84,'Строгино',155450),(100,8.01,'Таганский',116744),(101,7.27,'Тверской',75378),(102,5.92,'Текстильщики',101712),(103,7.5,'Тёплый Стан',130413),(104,10.43,'Тимирязевский',81889),(105,11.27,'Тропарёво-Никулино',112814),(106,9.62,'Филёвский Парк',89513),(107,6.96,'Фили-Давыдково',111377),(108,10.08,'Хамовники',102730),(109,5.73,'Ховрино',80792),(110,17.18,'Хорошёво-Мнёвники',166804),(111,9.88,'Хорошёвский',56536),(112,8.43,'Царицыно',125356),(113,5.52,'Черёмушки',102619),(114,5.4,'Чертаново Северное',111875),(115,6.52,'Чертаново Центральное',112223),(116,9.38,'Чертаново Южное',143662),(117,7.69,'Щукино',105665),(118,25.54,'Южное Бутово',178274),(119,3.88,'Южное Медведково',81986),(120,7.94,'Южное Тушино',104464),(121,4.53,'Южнопортовый',71747),(122,4.8,'Якиманка',26578),(123,7.99,'Ярославский',94245),(124,25.37,'Ясенево',174832),(125,25.6,'Внуковское',3988),(126,206.26,'Вороновское',8139),(127,24.77,'Воскресенское',6872),(128,52.96,'Десёновское',13748),(129,56.5,'Киевский',8318),(130,58.3,'Клёновское',2659),(131,8.28,'Кокошкино',11880),(132,87.78,'Краснопахорское',4026),(133,50.63,'Марушкинское',5472),(134,63.47,'Михайлово-Ярцевское',4887),(135,40.6,'Московский',20901),(136,6.41,'Мосрентген',17004),(137,156.75,'Новофёдоровское',6034),(138,118.94,'Первомайское',7237),(139,175.95,'Роговское',2613),(140,41.41,'Рязановское',16500),(141,67.07,'Сосенское',9199),(142,16.33,'Троицк',39873),(143,35.77,'Филимонковское',6217),(144,86.06,'Щаповское',7029),(145,7.62,'Щербинка',32450),(146,5.83,'Академический',106466),(153,748,'Раенчик',974);
/*!40000 ALTER TABLE `district` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-15 20:18:02
