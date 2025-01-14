-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2025 at 10:27 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `_2210010335_agama`
--

-- --------------------------------------------------------

--
-- Table structure for table `mustahik`
--

CREATE TABLE `mustahik` (
  `kd_mustahik` varchar(15) NOT NULL,
  `nama_mustahik` varchar(50) NOT NULL,
  `nik` varchar(15) NOT NULL,
  `tempat` varchar(50) NOT NULL,
  `tgl_lahir` varchar(15) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `jk` varchar(15) NOT NULL,
  `golongan` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mustahik`
--

INSERT INTO `mustahik` (`kd_mustahik`, `nama_mustahik`, `nik`, `tempat`, `tgl_lahir`, `alamat`, `jk`, `golongan`) VALUES
('1243515', 'bai', '1241', '1234', '235', '154', '1234', '1324'),
('321', 'baihaqi', '303030', 'banjarmasin', '30 maret 2004', 'sungai andai', 'laki laki', 'AB');

-- --------------------------------------------------------

--
-- Table structure for table `muzaki`
--

CREATE TABLE `muzaki` (
  `kd_muzaki` varchar(12) NOT NULL,
  `nama_muzaki` varchar(50) NOT NULL,
  `tempat` varchar(30) NOT NULL,
  `tgl_lahir` varchar(20) NOT NULL,
  `alamatlengkap` varchar(100) NOT NULL,
  `jk` varchar(10) NOT NULL,
  `nik` varchar(15) NOT NULL,
  `pekerjaan` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `penghasilan` varchar(20) NOT NULL,
  `telp` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `muzaki`
--

INSERT INTO `muzaki` (`kd_muzaki`, `nama_muzaki`, `tempat`, `tgl_lahir`, `alamatlengkap`, `jk`, `nik`, `pekerjaan`, `status`, `penghasilan`, `telp`, `email`) VALUES
('1241', 'baihaqi', '124', '5215', '235', '124', '125', '512', '124', '124', '512', '125');

-- --------------------------------------------------------

--
-- Table structure for table `zakat`
--

CREATE TABLE `zakat` (
  `kd_zakat` varchar(15) NOT NULL,
  `nama_zakat` varchar(30) NOT NULL,
  `bentuk` varchar(10) NOT NULL,
  `saldo` varchar(20) NOT NULL,
  `keterangan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `zakat`
--

INSERT INTO `zakat` (`kd_zakat`, `nama_zakat`, `bentuk`, `saldo`, `keterangan`) VALUES
('9988', 'fitrah', 'uang', '10000000', 'zakat');

-- --------------------------------------------------------

--
-- Table structure for table `zakatkeluar`
--

CREATE TABLE `zakatkeluar` (
  `no_keluar` varchar(15) NOT NULL,
  `kd_zakat` varchar(15) NOT NULL,
  `kd_mustahik` varchar(12) NOT NULL,
  `jmlh_keluar` varchar(15) NOT NULL,
  `bentuk` varchar(15) NOT NULL,
  `tgl_masuk` varchar(15) NOT NULL,
  `ket` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `zakatkeluar`
--

INSERT INTO `zakatkeluar` (`no_keluar`, `kd_zakat`, `kd_mustahik`, `jmlh_keluar`, `bentuk`, `tgl_masuk`, `ket`) VALUES
('9986', '3030', '132', '100', 'beras', '30', 'beras');

-- --------------------------------------------------------

--
-- Table structure for table `zakatmasuk`
--

CREATE TABLE `zakatmasuk` (
  `no_masuk` varchar(20) NOT NULL,
  `kd_zakat` varchar(15) NOT NULL,
  `kd_muzaki` varchar(12) NOT NULL,
  `jmlh_masuk` varchar(15) NOT NULL,
  `bentuk` varchar(15) NOT NULL,
  `tgl_masuk` varchar(15) NOT NULL,
  `norek` varchar(20) NOT NULL,
  `ket` varchar(100) NOT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `zakatmasuk`
--

INSERT INTO `zakatmasuk` (`no_masuk`, `kd_zakat`, `kd_muzaki`, `jmlh_masuk`, `bentuk`, `tgl_masuk`, `norek`, `ket`, `status`) VALUES
('999', '3030', '1234', '100', 'uang', '30', '123123123', 'zakat', 'done');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mustahik`
--
ALTER TABLE `mustahik`
  ADD PRIMARY KEY (`kd_mustahik`);

--
-- Indexes for table `muzaki`
--
ALTER TABLE `muzaki`
  ADD PRIMARY KEY (`kd_muzaki`);

--
-- Indexes for table `zakat`
--
ALTER TABLE `zakat`
  ADD PRIMARY KEY (`kd_zakat`);

--
-- Indexes for table `zakatkeluar`
--
ALTER TABLE `zakatkeluar`
  ADD PRIMARY KEY (`no_keluar`);

--
-- Indexes for table `zakatmasuk`
--
ALTER TABLE `zakatmasuk`
  ADD PRIMARY KEY (`no_masuk`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
