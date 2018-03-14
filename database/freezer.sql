-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 06, 2018 at 08:38 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.0.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `freezer`
--

-- --------------------------------------------------------

--
-- Table structure for table `Description_freezer`
--

CREATE TABLE `Description_freezer` (
  `freezer_id` int(11) NOT NULL,
  `number_boxes` int(11) NOT NULL,
  `freezer_name` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Description_freezer`
--

INSERT INTO `Description_freezer` (`freezer_id`, `number_boxes`, `freezer_name`) VALUES
(1, 4, 'xyz');

-- --------------------------------------------------------

--
-- Table structure for table `Description_product`
--

CREATE TABLE `Description_product` (
  `descr_id` int(11) NOT NULL,
  `product_name` varchar(256) NOT NULL,
  `text_descr` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Description_product`
--

INSERT INTO `Description_product` (`descr_id`, `product_name`, `text_descr`) VALUES
(1, 'glace citron', 'Glace maison au citron vert'),
(2, 'glace vanille', 'glace maison au aromatisÃ©e Ã  la vanille'),
(3, 'soupe tomate', 'value1'),
(4, 'Soupe de NoÃ«l', 'Soupe Ã  base de tomate, brocolli et poisson'),
(5, 'soupe champignon', 'soupe aux champignons des bois');

-- --------------------------------------------------------

--
-- Table structure for table `Description_type`
--

CREATE TABLE `Description_type` (
  `type_id` int(11) NOT NULL,
  `type_name_en` varchar(128) NOT NULL,
  `type_name_fr` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Description_type`
--

INSERT INTO `Description_type` (`type_id`, `type_name_en`, `type_name_fr`) VALUES
(1, 'soup', 'soupe'),
(2, 'meal soup', 'soupe repas'),
(3, 'meal soup (vegetable)', 'soupe repas (lÃ©gume)'),
(4, 'meal soup (meat)', 'soupe repas (viande)'),
(5, 'meal soup (fish)', 'soupe repas (poisson)'),
(6, 'read meat', 'viande rouge'),
(7, 'white meat', 'viande blanche'),
(8, 'black meat', 'viande noire'),
(9, 'exotic meat', 'viande exotique'),
(10, 'giblets', 'abats'),
(11, 'prepared meat', 'viande prÃ©parÃ©e'),
(12, 'BBQ meat', 'viande BBQ'),
(13, 'fish', 'poisson'),
(14, 'prepared fish', 'poisson prÃ©parÃ©'),
(15, 'shellfish', 'crustacÃ©s'),
(16, 'industrial prepared meal', 'plat prÃ©parÃ© industriel'),
(17, 'industrial prepared meal (vegetable)', 'plat prÃ©parÃ© industriel (lÃ©gume)'),
(18, 'industrial prepared meal (meat)', 'plat prÃ©parÃ© industriel (viande)'),
(19, 'industrial prepared meal (poisson)', 'plat prÃ©parÃ© industriel (poisson)'),
(20, 'homemade prepared dish', 'plat prÃ©parÃ© maison'),
(21, 'homemade prepared dish (vegetable)', 'plat prÃ©parÃ© maison (lÃ©gume)'),
(22, 'homemade prepared dish (meat)', 'plat prÃ©parÃ© maison (viande)'),
(23, 'homemade prepared dish (fish)', 'plat prÃ©parÃ© maison (poisson)'),
(24, 'ice-cream', 'glace'),
(25, 'sorbet', 'sorbet'),
(26, 'ice cubes', 'glaÃ§ons'),
(27, 'bread', 'pain'),
(28, 'fruit', 'fruits'),
(29, 'sauces', 'sauces'),
(30, 'cakes', 'gateaux'),
(31, 'pies', 'tartes'),
(32, 'pastry', 'viennoiseries'),
(33, 'pizza', 'pizza'),
(34, 'quiches', 'quiches'),
(35, 'spices', 'Ã©pices'),
(36, 'zakouski', 'zakouski'),
(37, 'dairy products', 'produit laitiers'),
(38, 'cheese', 'fromage'),
(39, 'butter', 'beurre'),
(40, 'dessert', 'dessert'),
(41, 'fried food', 'fritures'),
(42, 'not consumable', 'non consommable');

-- --------------------------------------------------------

--
-- Table structure for table `List_freezer`
--

CREATE TABLE `List_freezer` (
  `freezer_id` int(11) NOT NULL,
  `token` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `List_freezer`
--

INSERT INTO `List_freezer` (`freezer_id`, `token`) VALUES
(1, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92');

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `prod_id` int(11) NOT NULL,
  `token` varchar(128) NOT NULL,
  `descr_id` int(11) NOT NULL,
  `freezer_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  `date_in` date NOT NULL,
  `date_out` date DEFAULT NULL,
  `period` int(11) NOT NULL,
  `box_num` int(11) NOT NULL,
  `prod_num` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`prod_id`, `token`, `descr_id`, `freezer_id`, `type_id`, `date_in`, `date_out`, `period`, `box_num`, `prod_num`, `quantity`) VALUES
(1, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 1, 1, 24, '2016-03-02', NULL, 6, 1, 1, 1),
(2, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 2, 1, 24, '2016-12-31', '2017-03-02', 6, 1, 2, 1),
(3, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 3, 1, 1, '2017-12-26', NULL, 6, 1, 3, 4),
(4, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 4, 1, 1, '2017-12-26', NULL, 6, 1, 4, 4),
(5, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 5, 1, 1, '2018-02-01', NULL, 1, 1, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Product_to_type`
--

CREATE TABLE `Product_to_type` (
  `descr_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Product_to_type`
--

INSERT INTO `Product_to_type` (`descr_id`, `type_id`) VALUES
(1, 24),
(2, 24),
(3, 1),
(4, 1),
(5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `token` varchar(128) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `language` varchar(32) NOT NULL,
  `learning` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`token`, `password`, `email`, `language`, `learning`) VALUES
('5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', '93M3b3Q5EUbx6', 'loiclejoly@gmail.com', 'en', '[0,0]'),
('8f25fc89542722d26c5cb5bedb4fe05dc123128f7fcd44a3a5a8d7938b8d62c5', 'll', 'trolo', 'volvo', ''),
('b38c2f0294738c65d7e9f4a1bc0e5f5641e30d547da65e4752324ca933152c67', '93KM1.Jpwo.rQ', 'blabla', 'en', '[0,0]'),
('deb2e8ce824bc6e618b10aa2645e816696048f03ec446c6e7f274475b61671d5', 'de', 'de', 'fr', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Description_freezer`
--
ALTER TABLE `Description_freezer`
  ADD PRIMARY KEY (`freezer_id`);

--
-- Indexes for table `Description_product`
--
ALTER TABLE `Description_product`
  ADD PRIMARY KEY (`descr_id`);

--
-- Indexes for table `Description_type`
--
ALTER TABLE `Description_type`
  ADD PRIMARY KEY (`type_id`);

--
-- Indexes for table `List_freezer`
--
ALTER TABLE `List_freezer`
  ADD PRIMARY KEY (`freezer_id`,`token`),
  ADD KEY `token` (`token`);

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`prod_id`),
  ADD KEY `descr_id` (`descr_id`),
  ADD KEY `freezer_id` (`freezer_id`),
  ADD KEY `type_id` (`type_id`),
  ADD KEY `token` (`token`);

--
-- Indexes for table `Product_to_type`
--
ALTER TABLE `Product_to_type`
  ADD PRIMARY KEY (`descr_id`,`type_id`),
  ADD KEY `type_id` (`type_id`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`token`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Description_freezer`
--
ALTER TABLE `Description_freezer`
  MODIFY `freezer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Description_product`
--
ALTER TABLE `Description_product`
  MODIFY `descr_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Description_type`
--
ALTER TABLE `Description_type`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `prod_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `List_freezer`
--
ALTER TABLE `List_freezer`
  ADD CONSTRAINT `List_freezer_ibfk_1` FOREIGN KEY (`freezer_id`) REFERENCES `Description_freezer` (`freezer_id`),
  ADD CONSTRAINT `List_freezer_ibfk_2` FOREIGN KEY (`token`) REFERENCES `User` (`token`);

--
-- Constraints for table `Product`
--
ALTER TABLE `Product`
  ADD CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`descr_id`) REFERENCES `Description_product` (`descr_id`),
  ADD CONSTRAINT `Product_ibfk_2` FOREIGN KEY (`freezer_id`) REFERENCES `Description_freezer` (`freezer_id`),
  ADD CONSTRAINT `Product_ibfk_3` FOREIGN KEY (`type_id`) REFERENCES `Description_type` (`type_id`),
  ADD CONSTRAINT `Product_ibfk_4` FOREIGN KEY (`token`) REFERENCES `User` (`token`);

--
-- Constraints for table `Product_to_type`
--
ALTER TABLE `Product_to_type`
  ADD CONSTRAINT `Product_to_type_ibfk_1` FOREIGN KEY (`descr_id`) REFERENCES `Description_product` (`descr_id`),
  ADD CONSTRAINT `Product_to_type_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `Description_type` (`type_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
