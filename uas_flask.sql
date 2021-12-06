-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 06, 2021 at 09:16 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uas_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `iduser` int(3) NOT NULL,
  `namalengkap` varchar(40) NOT NULL,
  `username` varchar(6) NOT NULL,
  `password` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`iduser`, `namalengkap`, `username`, `password`) VALUES
(1, 'Dimas Putra Widiyanto', 'prom11', 'admin'),
(6, 'Satya Pamungkas', 'satya', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `idpost` int(3) NOT NULL,
  `judul` varchar(40) NOT NULL,
  `isi` text NOT NULL,
  `keyword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`idpost`, `judul`, `isi`, `keyword`) VALUES
(142, 'About me', 'Halooo, perkenalkan saya Dimas Putra Widiyanto sebagai pendiri website ini dan sebagai mahasiswa Politeknik LP3I Jakarta ツ', 'Life'),
(143, 'Kbear Lark', '“Larks are one of the most adaptable species of birds out there, they can produce that melodious and high pitch singing especially on their call to mating ritual and even to a simplest communication, they can mimic some of other birds\' chirping and churrs too.”', 'Audio'),
(144, 'Moondrop Aria 2021', 'Aria adopts 10mm diameter dual-cavity magnetic high-performance dynamic driver, and the whole LCP (Liquid Crystal Polymer) liquid crystal diaphragm to bring excellent transient response and high-resolution sound details.', 'Audio'),
(145, 'GTA The Trilogy – The Definitive Edition', 'GTA alias Grand Theft Auto merupakan franchise milik Rockstar Games di bawah Take Two Interactive yang menjadikan genre action open-world sebagai basis. Ceritanya seringkali memosisikan karakter utama Anda sebagai tokoh kriminal yang terlibat dalam banyak aksi kejahatan, baik yang terbuka ataupun tidak. Karakterisasi keren, misi yang asyik, pilihan musik yang solid, dan beragam inovasi yang disuntikkan dari satu seri ke seri lainnya selalu membuat seri ini sukses.', 'Video Game');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`iduser`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`idpost`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `iduser` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `idpost` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=147;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
