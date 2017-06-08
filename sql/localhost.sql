-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 24, 2017 at 12:36 PM
-- Server version: 5.5.54-0+deb8u1
-- PHP Version: 5.6.30-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `craigslistdb`
--
-- DROP DATABASE `craigslistdb`;

-- --------------------------------------------------------

--
-- Stand-in structure for view `One Day`
--
CREATE TABLE IF NOT EXISTS `One Day` (
`serial` int(11)
,`scrap_date` timestamp
,`posturl` text
,`time` text
,`posttitle` text
,`parse_posts` text
);
-- --------------------------------------------------------

--
-- Stand-in structure for view `Two days`
--
CREATE TABLE IF NOT EXISTS `Two days` (
`serial` int(11)
,`scrap_date` timestamp
,`posturl` text
,`time` text
,`posttitle` text
,`parse_posts` text
);
-- --------------------------------------------------------

--
-- Table structure for table `cjposts`
--

CREATE TABLE IF NOT EXISTS `cjposts` (
`serial` int(11) NOT NULL,
  `scrap_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `posturl` text NOT NULL,
  `time` text NOT NULL,
  `posttitle` text NOT NULL,
  `parse_posts` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=10099 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cjposts`
--
ALTER TABLE `cjposts`
 ADD PRIMARY KEY (`serial`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cjposts`
--
ALTER TABLE `cjposts`
MODIFY `serial` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10099;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
