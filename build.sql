-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- Host: REDACTED
-- Generation Time: Jun 10, 2016 at 06:08 PM
-- Server version: 5.5.49-0ubuntu0.14.04.1
-- PHP Version: 5.3.28

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sql5122664`
--
CREATE DATABASE `alexa_chromecast` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sql5122664`;

-- --------------------------------------------------------

--
-- Table structure for table `commands`
--

CREATE TABLE IF NOT EXISTS `commands` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `command` varchar(99) COLLATE latin1_general_ci NOT NULL,
  `slot` varchar(99) COLLATE latin1_general_ci NOT NULL,
  `type_of_media` varchar(99) COLLATE latin1_general_ci NOT NULL,
  `TIMESTAMP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=117 ;

-- --------------------------------------------------------

--
-- Table structure for table `saved_chromecasts`
--

CREATE TABLE IF NOT EXISTS `saved_chromecasts` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `friendly_name` varchar(999) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
