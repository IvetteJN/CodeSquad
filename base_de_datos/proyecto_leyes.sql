-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `leyes`
--

DROP TABLE IF EXISTS `leyes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leyes` (
  `id_leyes` int NOT NULL AUTO_INCREMENT,
  `nro_leyes` int NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  `categoria` varchar(35) NOT NULL,
  `jurisdiccion` varchar(35) NOT NULL,
  `or_legislativo` varchar(200) NOT NULL,
  `palabra_clave` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_leyes`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leyes`
--

LOCK TABLES `leyes` WRITE;
/*!40000 ALTER TABLE `leyes` DISABLE KEYS */;
INSERT INTO `leyes` VALUES (1,20774,'1974-09-29','Esta ley regula las relaciones laborales entre empleadores y empleados en el país. Establece los derechos y obligaciones laborales, abarcando temas como contratación, remuneración, horarios, vacaciones, licencias y protección laboral. Su objetivo es proteger los derechos de los trabajadores y promover condiciones laborales justas y equitativas.','Laboral.','Nacional.','Congreso de la Nación.','Teletrabajo, Trabajo remoto, Derechos laborales, Obligaciones laborales, Jornada laboral, Desconexión digital, Compensación de gastos, Salud y seguridad laboral\nAcuerdo de teletrabajo.'),(2,27555,'2020-07-14','Esta ley establece los derechos y obligaciones tanto de los empleadores como de los trabajadores en el ámbito del teletrabajo. Aborda aspectos como la jornada laboral, la desconexión digital, la compensación de gastos y la protección de la salud y seguridad laboral. Su objetivo es garantizar condiciones justas y equitativas para los trabajadores que desempeñan sus labores de forma remota.','Laboral','Nacional','Congreso de la nación','Teletrabajo, Trabajo remoto, Derechos laborales, Obligaciones laborales, Jornada laboral, Desconexión digital, Compensación de gastos, Salud y seguridad laboral\nAcuerdo de teletrabajo.'),(3,7642,'1987-11-21','Esta ley regula la práctica de la profesión de informática en la provincia de Córdoba, estableciendo requisitos y normas para los profesionales de este campo. Su objetivo es garantizar la calidad y el cumplimiento ético de los servicios informáticos en la región.  Ademas de establecer entre los profesionales de Ciencias Informáticas una comunidad de intereses e ideales éticos, normativos y profesionales a fin de propender a su continuo perfeccionamiento.','Derecho profesional','Provincial','Legislatura de Córdoba','Matriculación, Ciencias Informaticas, Informatica, Ejercicio profesional, Titulos, Graduados, Ética, Profesional en Informatica, Deberes del profesional, Consejo, Tribunal de disciplina.');
/*!40000 ALTER TABLE `leyes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-22 11:15:50
