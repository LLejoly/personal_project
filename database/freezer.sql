-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 21, 2018 at 10:50 AM
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
  `freezer_id` int(32) NOT NULL,
  `number_boxes` int(32) NOT NULL,
  `freezer_name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Description_freezer`
--

INSERT INTO `Description_freezer` (`freezer_id`, `number_boxes`, `freezer_name`) VALUES
(1, 4, 'frigo 1'),
(2, 8, 'frigo 2'),
(3, 4, 'frigo 3'),
(4, 4, 'frigo 4'),
(5, 3, 'frigo 5');

-- --------------------------------------------------------

--
-- Table structure for table `Description_product`
--

CREATE TABLE `Description_product` (
  `descr_id` int(32) NOT NULL,
  `product_name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `text_descr` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Description_product`
--

INSERT INTO `Description_product` (`descr_id`, `product_name`, `text_descr`) VALUES
(1, 'Glace au citron', 'Glace maison au citron vert'),
(2, 'glace vanille', 'glace maison au aromatisée à la vanille'),
(3, 'soupe tomate', 'value1'),
(4, 'Soupe de Noël', 'Soupe à base de tomate, brocolli et poisson'),
(5, 'soupe champignon', 'soupe aux champignons des bois'),
(6, 'glace cookies', 'glace vanille aux cookies dough'),
(7, 'sorbet citron', 'sorbet citron'),
(8, 'sorbet tomate', 'sorbet à base de tomate et aux épices'),
(9, 'sorbet melon', 'sorbet à base de melons '),
(10, 'sorbet fraise', 'sorbet à base de fraise du jardin'),
(11, 'sorbet aux herbes aromatiques', 'sorbet à base de basilic et de thym'),
(12, 'glace moka', 'glace moka'),
(13, 'glace vanille', 'glace à la vanille de Madagascar'),
(14, 'filet de dinde', 'filet de dinde cuit'),
(15, 'lapin', 'lapin'),
(16, 'filet de porc', 'filet de porc'),
(17, 'filet de veau', 'filet de veau'),
(18, 'cabillaud', 'filet de cabillaud premium'),
(19, 'filet de sole', 'filet de  sole meunière premium'),
(20, 'pommes', 'récolte de pommes de l\'arbre du jardin'),
(21, 'pommes de terre', 'récolte de pommes de terre du potager'),
(22, 'carottes', 'carottes du jardin'),
(23, 'choux', 'choux rouge du jardin'),
(24, 'épinards', 'épinards frais du jardin'),
(25, 'soupe repas cabillaud', 'Soupe repas au poisson cabillaud et légumes de saison'),
(26, 'soupe repas des andes', 'soupe raps à base de boulgour, lentilles et légumes'),
(27, 'basilic', 'basilic frais'),
(28, 'Thym', 'Thym frais'),
(29, 'Sauge', 'Sauge fraiche'),
(30, 'pralines de tonka', 'Pralines à la fève de tonka'),
(31, 'Magnum à l\\\'amande', 'Magnum à l\'amande'),
(32, 'Moelleux au chocolat', 'Moelleux au chocolat fait maison'),
(33, 'marinade de porc', 'marinade de porc façon provencale'),
(34, 'canard mariné', 'carnard mariné pour bqq'),
(35, 'Brochettes marinées', 'brochettes marinées curry'),
(36, 'Brochettes marinées', 'brochettes marinées paprika'),
(37, 'Brochettes de dinde', 'brochettes marinées paprika'),
(38, 'Brochettes de dinde', 'brochettes marinées curry'),
(39, 'Soupe tomate', 'soupe à la tomate verte'),
(40, 'Soupe façon grand-mère', 'soupe aux vieux légumes'),
(41, 'Soupe aux poireaux', 'soupe aux poireaux du jarin'),
(42, 'Soupe aux épinards', 'soupe aux épinards du jarin'),
(43, 'Soupe aux légumes oubliés', 'Soupe aux légumes oubliés'),
(44, 'Soupe aux potirons', 'Soupe aux potirons'),
(45, 'Soupe aux courges', 'Soupe aux courges'),
(46, 'Boudins', 'petits boudins'),
(47, 'Saucisses campagne', 'saucisse campagnes'),
(48, 'Saucisses à l\\\'orval', 'saucisse à la bière d\\\'orval');

-- --------------------------------------------------------

--
-- Table structure for table `Description_type`
--

CREATE TABLE `Description_type` (
  `type_id` int(32) NOT NULL,
  `type_name_en` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type_name_fr` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Description_type`
--

INSERT INTO `Description_type` (`type_id`, `type_name_en`, `type_name_fr`) VALUES
(1, 'soup', 'soupe'),
(2, 'meal soup', 'soupe repas'),
(3, 'meal soup (vegetable)', 'soupe repas (légume)'),
(4, 'meal soup (meat)', 'soupe repas (viande)'),
(5, 'meal soup (fish)', 'soupe repas (poisson)'),
(6, 'read meat', 'viande rouge'),
(7, 'white meat', 'viande blanche'),
(8, 'black meat', 'viande noire'),
(9, 'exotic meat', 'viande exotique'),
(10, 'giblets', 'abats'),
(11, 'prepared meat', 'viande préparée'),
(12, 'BBQ meat', 'viande BBQ'),
(13, 'fish', 'poisson'),
(14, 'prepared fish', 'poisson préparé'),
(15, 'shellfish', 'crustacés'),
(16, 'industrial prepared meal', 'plat préparé industriel'),
(17, 'industrial prepared meal (vegetable)', 'plat préparé industriel (légume)'),
(18, 'industrial prepared meal (meat)', 'plat préparé industriel (viande)'),
(19, 'industrial prepared meal (poisson)', 'plat préparé industriel (poisson)'),
(20, 'homemade prepared dish', 'plat préparé maison'),
(21, 'homemade prepared dish (vegetable)', 'plat préparé maison (légume)'),
(22, 'homemade prepared dish (meat)', 'plat préparé maison (viande)'),
(23, 'homemade prepared dish (fish)', 'plat préparé maison (poisson)'),
(24, 'ice-cream', 'glace'),
(25, 'sorbet', 'sorbet'),
(26, 'ice cubes', 'glaçons'),
(27, 'bread', 'pain'),
(28, 'fruit', 'fruits'),
(29, 'sauces', 'sauces'),
(30, 'cakes', 'gateaux'),
(31, 'pies', 'tartes'),
(32, 'pastry', 'viennoiseries'),
(33, 'pizza', 'pizza'),
(34, 'quiches', 'quiches'),
(35, 'spices', 'épices'),
(36, 'zakouski', 'zakouski'),
(37, 'dairy products', 'produit laitiers'),
(38, 'cheese', 'fromage'),
(39, 'butter', 'beurre'),
(40, 'dessert', 'dessert'),
(41, 'fried food', 'fritures'),
(42, 'not consumable', 'non consommable'),
(43, 'vegetable', 'légume');

-- --------------------------------------------------------

--
-- Table structure for table `List_freezer`
--

CREATE TABLE `List_freezer` (
  `freezer_id` int(32) NOT NULL,
  `token` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `List_freezer`
--

INSERT INTO `List_freezer` (`freezer_id`, `token`) VALUES
(1, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'),
(2, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'),
(3, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'),
(4, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'),
(5, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92');

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `prod_id` int(32) NOT NULL,
  `token` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descr_id` int(32) NOT NULL,
  `freezer_id` int(32) NOT NULL,
  `type_id` int(32) NOT NULL,
  `date_in` date NOT NULL,
  `date_out` date DEFAULT NULL,
  `period` int(32) NOT NULL,
  `box_num` int(32) NOT NULL,
  `prod_num` int(32) NOT NULL,
  `quantity` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`prod_id`, `token`, `descr_id`, `freezer_id`, `type_id`, `date_in`, `date_out`, `period`, `box_num`, `prod_num`, `quantity`) VALUES
(1, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 1, 1, 24, '2016-03-02', '2016-06-02', 10, 1, 1, 10),
(2, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 2, 1, 24, '2016-12-31', '2017-03-02', 6, 1, 2, 1),
(3, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 3, 1, 1, '2017-12-26', '2018-02-05', 6, 1, 3, 4),
(4, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 4, 1, 1, '2017-12-26', NULL, 6, 1, 4, 4),
(5, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 5, 1, 1, '2018-02-01', NULL, 1, 1, 5, 1),
(6, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 6, 1, 24, '2018-01-29', NULL, 12, 1, 6, 2),
(7, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 7, 2, 25, '2017-09-10', NULL, 12, 1, 1, 4),
(8, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 8, 2, 25, '2017-09-10', NULL, 12, 1, 2, 4),
(9, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 9, 2, 25, '2017-06-17', NULL, 12, 2, 1, 3),
(10, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 10, 2, 25, '2017-08-13', NULL, 12, 1, 3, 2),
(11, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 11, 2, 25, '2017-07-23', NULL, 12, 1, 4, 2),
(12, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 12, 1, 24, '2017-07-23', NULL, 12, 2, 2, 3),
(13, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 13, 1, 24, '2017-07-23', NULL, 12, 1, 2, 3),
(14, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 14, 1, 7, '2017-05-23', NULL, 24, 2, 1, 1),
(15, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 15, 2, 7, '2017-10-03', NULL, 24, 2, 2, 3),
(16, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 16, 1, 7, '2017-06-17', NULL, 24, 3, 1, 3),
(17, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 17, 1, 7, '2017-11-30', NULL, 12, 4, 1, 3),
(18, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 18, 1, 13, '2017-09-02', NULL, 12, 4, 2, 2),
(19, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 19, 2, 13, '2017-09-02', NULL, 12, 4, 1, 2),
(20, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 20, 1, 28, '2017-09-15', NULL, 24, 3, 2, 6),
(21, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 21, 1, 43, '2017-06-18', NULL, 24, 3, 3, 4),
(22, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 22, 2, 43, '2017-11-12', NULL, 12, 2, 3, 4),
(23, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 23, 2, 43, '2017-10-09', NULL, 12, 2, 4, 3),
(24, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 24, 2, 43, '2017-09-17', NULL, 12, 2, 5, 4),
(25, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 25, 2, 5, '2017-09-13', NULL, 12, 2, 6, 4),
(26, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 26, 2, 3, '2017-08-23', NULL, 12, 2, 7, 4),
(27, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 27, 2, 35, '2017-08-23', NULL, 36, 2, 8, 4),
(28, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 28, 2, 35, '2017-08-23', NULL, 36, 2, 9, 4),
(29, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 29, 2, 35, '2017-08-23', NULL, 36, 2, 10, 4),
(30, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 30, 2, 40, '2017-08-23', NULL, 36, 2, 11, 4),
(31, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 31, 2, 40, '2017-11-12', NULL, 36, 2, 12, 4),
(32, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 32, 2, 40, '2017-06-14', NULL, 36, 2, 13, 8),
(33, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 33, 2, 7, '2018-03-17', NULL, 24, 3, 1, 4),
(34, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 34, 1, 12, '2018-03-11', NULL, 24, 1, 1, 4),
(35, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 35, 2, 12, '2018-04-21', NULL, 24, 1, 5, 4),
(36, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 36, 2, 12, '2017-10-15', NULL, 24, 1, 6, 4),
(37, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 37, 2, 12, '2017-09-17', NULL, 24, 1, 7, 4),
(38, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 38, 2, 12, '2017-08-23', NULL, 24, 1, 8, 4),
(39, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 39, 2, 1, '2017-08-23', NULL, 24, 1, 9, 4),
(40, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 40, 2, 1, '2017-08-23', NULL, 24, 1, 10, 4),
(41, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 41, 2, 1, '2017-07-17', NULL, 24, 1, 11, 4),
(42, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 42, 2, 1, '2017-06-09', NULL, 24, 1, 12, 4),
(43, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 43, 2, 1, '2017-09-19', NULL, 24, 1, 13, 4),
(44, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 44, 2, 1, '2017-10-26', NULL, 24, 1, 14, 4),
(45, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 45, 2, 1, '2017-11-14', NULL, 24, 1, 15, 4),
(46, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 46, 2, 12, '2017-07-05', NULL, 24, 3, 2, 4),
(47, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 47, 2, 12, '2017-07-05', NULL, 24, 3, 3, 4),
(48, '5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', 48, 2, 12, '2017-07-05', NULL, 24, 3, 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Product_to_type`
--

CREATE TABLE `Product_to_type` (
  `descr_id` int(32) NOT NULL,
  `type_id` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Product_to_type`
--

INSERT INTO `Product_to_type` (`descr_id`, `type_id`) VALUES
(1, 24),
(2, 24),
(3, 1),
(4, 1),
(5, 1),
(6, 24),
(7, 25),
(8, 25),
(9, 25),
(10, 25),
(11, 25),
(12, 24),
(13, 24),
(14, 7),
(15, 7),
(16, 7),
(17, 7),
(18, 13),
(19, 13),
(20, 28),
(21, 43),
(22, 43),
(23, 43),
(24, 43),
(25, 5),
(26, 3),
(27, 35),
(28, 35),
(29, 35),
(30, 40),
(31, 40),
(32, 40),
(33, 7),
(34, 12),
(35, 12),
(36, 12),
(37, 12),
(38, 12),
(39, 1),
(40, 1),
(41, 1),
(42, 1),
(43, 1),
(44, 1),
(45, 1),
(46, 12),
(47, 12),
(48, 12);

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `token` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `language` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `learning` longtext COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`token`, `password`, `email`, `language`, `learning`) VALUES
('1f149b786e59fefd32e1cdda6692bf83ea34307771938e06753f22b57205aea6', '93KM1.Jpwo.rQ', 'test2', 'en', '[0,0]'),
('5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92', '93ZLh7XBn8r6w', 'test@gmail.com', 'en', '[0,0]');

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
  MODIFY `freezer_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Description_product`
--
ALTER TABLE `Description_product`
  MODIFY `descr_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `Description_type`
--
ALTER TABLE `Description_type`
  MODIFY `type_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `prod_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

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
