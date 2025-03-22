-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2024 at 12:12 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online cafe`
--

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `Area_id` int(11) NOT NULL,
  `Area_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`Area_id`, `Area_name`) VALUES
(1, 'Naranpura');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add area', 7, 'add_area'),
(26, 'Can change area', 7, 'change_area'),
(27, 'Can delete area', 7, 'delete_area'),
(28, 'Can view area', 7, 'view_area'),
(29, 'Can add cafe_ table', 8, 'add_cafe_table'),
(30, 'Can change cafe_ table', 8, 'change_cafe_table'),
(31, 'Can delete cafe_ table', 8, 'delete_cafe_table'),
(32, 'Can view cafe_ table', 8, 'view_cafe_table'),
(33, 'Can add category', 9, 'add_category'),
(34, 'Can change category', 9, 'change_category'),
(35, 'Can delete category', 9, 'delete_category'),
(36, 'Can view category', 9, 'view_category'),
(37, 'Can add contactus', 10, 'add_contactus'),
(38, 'Can change contactus', 10, 'change_contactus'),
(39, 'Can delete contactus', 10, 'delete_contactus'),
(40, 'Can view contactus', 10, 'view_contactus'),
(41, 'Can add customer', 11, 'add_customer'),
(42, 'Can change customer', 11, 'change_customer'),
(43, 'Can delete customer', 11, 'delete_customer'),
(44, 'Can view customer', 11, 'view_customer'),
(45, 'Can add order', 12, 'add_order'),
(46, 'Can change order', 12, 'change_order'),
(47, 'Can delete order', 12, 'delete_order'),
(48, 'Can view order', 12, 'view_order'),
(49, 'Can add product', 13, 'add_product'),
(50, 'Can change product', 13, 'change_product'),
(51, 'Can delete product', 13, 'delete_product'),
(52, 'Can view product', 13, 'view_product'),
(53, 'Can add order_ item', 14, 'add_order_item'),
(54, 'Can change order_ item', 14, 'change_order_item'),
(55, 'Can delete order_ item', 14, 'delete_order_item'),
(56, 'Can view order_ item', 14, 'view_order_item'),
(57, 'Can add feedback', 15, 'add_feedback'),
(58, 'Can change feedback', 15, 'change_feedback'),
(59, 'Can delete feedback', 15, 'delete_feedback'),
(60, 'Can view feedback', 15, 'view_feedback'),
(61, 'Can add cart table', 16, 'add_carttable'),
(62, 'Can change cart table', 16, 'change_carttable'),
(63, 'Can delete cart table', 16, 'delete_carttable'),
(64, 'Can view cart table', 16, 'view_carttable'),
(65, 'Can add table_booking', 17, 'add_table_booking'),
(66, 'Can change table_booking', 17, 'change_table_booking'),
(67, 'Can delete table_booking', 17, 'delete_table_booking'),
(68, 'Can view table_booking', 17, 'view_table_booking');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cafe_table`
--

CREATE TABLE `cafe_table` (
  `Table_id` int(11) NOT NULL,
  `Layout_Image` varchar(2000) NOT NULL,
  `No_of_seats` int(11) NOT NULL,
  `Avaibility_status` varchar(100) NOT NULL,
  `Description` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cafe_table`
--

INSERT INTO `cafe_table` (`Table_id`, `Layout_Image`, `No_of_seats`, `Avaibility_status`, `Description`) VALUES
(1, 'c7d65b44116250693891229d024ffc0a.jpeg', 8, '1', 'Table For 8');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `Quantity` int(10) UNSIGNED NOT NULL CHECK (`Quantity` >= 0),
  `Total` int(11) NOT NULL,
  `Customer_id_id` int(11) NOT NULL,
  `Product_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `Category_id` int(11) NOT NULL,
  `Category_Name` varchar(100) NOT NULL,
  `Description` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`Category_id`, `Category_Name`, `Description`) VALUES
(1, 'Pizza', '.');

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

CREATE TABLE `contactus` (
  `contact_id` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(254) NOT NULL,
  `Message` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Customer_id` int(11) NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Email` varchar(254) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Address` varchar(300) NOT NULL,
  `is_admin` varchar(50) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) NOT NULL,
  `Area_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Customer_id`, `First_Name`, `Last_Name`, `Email`, `Password`, `Phone`, `Address`, `is_admin`, `otp`, `otp_used`, `Area_id_id`) VALUES
(1, 'Harshil', 'Patel', 'harshilp316@gmail.com', 'Harshu@l1', '128683', '17, Base Society', '1', '0', 0, 1),
(2, 'Raj', 'Shah', 'deathp293@gmail.com', 'Harshu@l1', '32423', '18, Base Society', '0', '0', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'Cafe_admin', 'area'),
(8, 'Cafe_admin', 'cafe_table'),
(16, 'Cafe_admin', 'carttable'),
(9, 'Cafe_admin', 'category'),
(10, 'Cafe_admin', 'contactus'),
(11, 'Cafe_admin', 'customer'),
(15, 'Cafe_admin', 'feedback'),
(12, 'Cafe_admin', 'order'),
(14, 'Cafe_admin', 'order_item'),
(13, 'Cafe_admin', 'product'),
(17, 'Cafe_admin', 'table_booking'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Cafe_admin', '0001_initial', '2024-04-04 09:57:12.899496'),
(2, 'contenttypes', '0001_initial', '2024-04-04 09:57:12.939534'),
(3, 'auth', '0001_initial', '2024-04-04 09:57:13.588046'),
(4, 'admin', '0001_initial', '2024-04-04 09:57:13.708509'),
(5, 'admin', '0002_logentry_remove_auto_add', '2024-04-04 09:57:13.720535'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-04 09:57:13.732526'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-04-04 09:57:13.800077'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-04-04 09:57:13.860122'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-04-04 09:57:13.880136'),
(10, 'auth', '0004_alter_user_username_opts', '2024-04-04 09:57:13.888126'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-04-04 09:57:13.932161'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-04-04 09:57:13.936172'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-04-04 09:57:13.948285'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-04-04 09:57:13.964323'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-04-04 09:57:13.980323'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-04-04 09:57:13.996323'),
(17, 'auth', '0011_update_proxy_permissions', '2024-04-04 09:57:14.016326'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-04-04 09:57:14.032539'),
(19, 'sessions', '0001_initial', '2024-04-04 09:57:14.068057');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('y6s4siblbemu1l39lfl2dxwmxb41lukn', '.eJyrVkpMyc3Mi89MUbIy1IFyUnMTM3OUrJQyEouKMzJzCowNzRzSQWJ6yfm5SjBVBYnFxUBFHiBFpQ45hkq1AADfGjw:1rsJt7:pFeIMVNyKBYNGyrmVSCYhA2Q9S9jcZbAL5f15BjZP6M', '2024-04-18 10:00:05.802003'),
('yoxr669b0bkeka84tt4zi5jwz9q6ze1z', '.eJyrVkouLS7Jz00tis9MUbIy0kHwU3MTM3OUrJRSUhNLMgqMLI0d0kEiesn5uUpIygoSi4uBqjwSi4ozSh1yDJVqAfgiHZc:1rsJwh:AO7721rHlHcP3_Oa_YEpLjVuUQDf5IxhB3Iuns5yi0A', '2024-04-18 10:03:47.309283');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Feedback_id` int(11) NOT NULL,
  `Description` varchar(400) NOT NULL,
  `Feedback_date` date NOT NULL,
  `Customer_id_id` int(11) NOT NULL,
  `Product_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `Order_id` int(11) NOT NULL,
  `Order_Date` date NOT NULL,
  `Delivery_address` varchar(255) NOT NULL,
  `Total_Amount` int(11) NOT NULL,
  `Order_status` varchar(100) NOT NULL,
  `Payment_status` varchar(100) NOT NULL,
  `Payment_Mode` varchar(100) NOT NULL,
  `Delivery_status` varchar(100) NOT NULL,
  `Customer_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`Order_id`, `Order_Date`, `Delivery_address`, `Total_Amount`, `Order_status`, `Payment_status`, `Payment_Mode`, `Delivery_status`, `Customer_id_id`) VALUES
(1, '2024-04-04', '', 600, '0', '2', '', '', 2),
(2, '2024-04-04', '', 100, '0', '2', '', '', 2),
(3, '2024-04-04', '', 350, '0', '2', '', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `order_item`
--

CREATE TABLE `order_item` (
  `Order_Item_id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  `Order_id_id` int(11) NOT NULL,
  `Product_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_item`
--

INSERT INTO `order_item` (`Order_Item_id`, `Quantity`, `Price`, `Order_id_id`, `Product_id_id`) VALUES
(1, 2, 500, 1, 1),
(2, 1, 250, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_id` int(11) NOT NULL,
  `Product_Name` varchar(100) NOT NULL,
  `Price` int(11) NOT NULL,
  `Description` varchar(400) NOT NULL,
  `Product_image` varchar(2000) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Category_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_id`, `Product_Name`, `Price`, `Description`, `Product_image`, `Quantity`, `Category_id_id`) VALUES
(1, 'Pizza Mexicana', 250, 'Enjoy a taste of Mexico with Pizza Mexicana. This flavorful pie features a zesty tomato base topped with spicy salsa, savory seasoned meats, vibrant bell peppers, onions, and a generous sprinkling of melted cheese. Each bite is a fiesta of bold flavors, bringing the essence of Mexican cuisine to your pizza night.', 'pizza-mexicana-2-682x1024-1141953025.jpg', 50, 1);

-- --------------------------------------------------------

--
-- Table structure for table `table_booking`
--

CREATE TABLE `table_booking` (
  `Booking_id` int(11) NOT NULL,
  `Phonenumber` int(11) NOT NULL,
  `Booking_Date` date NOT NULL,
  `Booking_status` varchar(100) NOT NULL,
  `Booking_Time` time(6) NOT NULL,
  `NumberofPeople` int(11) NOT NULL,
  `Customer_id_id` int(11) NOT NULL,
  `Table_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`Area_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `cafe_table`
--
ALTER TABLE `cafe_table`
  ADD PRIMARY KEY (`Table_id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `Cart_Customer_id_id_1b45d80a_fk_Customer_Customer_id` (`Customer_id_id`),
  ADD KEY `Cart_Product_id_id_eb30c18d_fk_Product_Product_id` (`Product_id_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`Category_id`);

--
-- Indexes for table `contactus`
--
ALTER TABLE `contactus`
  ADD PRIMARY KEY (`contact_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Customer_id`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD KEY `Customer_Area_id_id_5499b88f_fk_Area_Area_id` (`Area_id_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`Feedback_id`),
  ADD KEY `Feedback_Customer_id_id_b57c60b3_fk_Customer_Customer_id` (`Customer_id_id`),
  ADD KEY `Feedback_Product_id_id_dc9ff513_fk_Product_Product_id` (`Product_id_id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`Order_id`),
  ADD KEY `Order_Customer_id_id_0cdc6f9a_fk_Customer_Customer_id` (`Customer_id_id`);

--
-- Indexes for table `order_item`
--
ALTER TABLE `order_item`
  ADD PRIMARY KEY (`Order_Item_id`),
  ADD KEY `Order_Item_Order_id_id_f4109a24_fk_Order_Order_id` (`Order_id_id`),
  ADD KEY `Order_Item_Product_id_id_fa4b618c_fk_Product_Product_id` (`Product_id_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`Product_id`),
  ADD KEY `Product_Category_id_id_94e10cf3_fk_Category_Category_id` (`Category_id_id`);

--
-- Indexes for table `table_booking`
--
ALTER TABLE `table_booking`
  ADD PRIMARY KEY (`Booking_id`),
  ADD KEY `Table_booking_Customer_id_id_9a2e449e_fk_Customer_Customer_id` (`Customer_id_id`),
  ADD KEY `Table_booking_Table_id_id_aa5d4ee6_fk_Cafe_Table_Table_id` (`Table_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `Area_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cafe_table`
--
ALTER TABLE `cafe_table`
  MODIFY `Table_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `Category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contactus`
--
ALTER TABLE `contactus`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `Customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `Feedback_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `Order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `order_item`
--
ALTER TABLE `order_item`
  MODIFY `Order_Item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `Product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `table_booking`
--
ALTER TABLE `table_booking`
  MODIFY `Booking_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `Cart_Customer_id_id_1b45d80a_fk_Customer_Customer_id` FOREIGN KEY (`Customer_id_id`) REFERENCES `customer` (`Customer_id`),
  ADD CONSTRAINT `Cart_Product_id_id_eb30c18d_fk_Product_Product_id` FOREIGN KEY (`Product_id_id`) REFERENCES `product` (`Product_id`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `Customer_Area_id_id_5499b88f_fk_Area_Area_id` FOREIGN KEY (`Area_id_id`) REFERENCES `area` (`Area_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `Feedback_Customer_id_id_b57c60b3_fk_Customer_Customer_id` FOREIGN KEY (`Customer_id_id`) REFERENCES `customer` (`Customer_id`),
  ADD CONSTRAINT `Feedback_Product_id_id_dc9ff513_fk_Product_Product_id` FOREIGN KEY (`Product_id_id`) REFERENCES `product` (`Product_id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `Order_Customer_id_id_0cdc6f9a_fk_Customer_Customer_id` FOREIGN KEY (`Customer_id_id`) REFERENCES `customer` (`Customer_id`);

--
-- Constraints for table `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `Order_Item_Order_id_id_f4109a24_fk_Order_Order_id` FOREIGN KEY (`Order_id_id`) REFERENCES `order` (`Order_id`),
  ADD CONSTRAINT `Order_Item_Product_id_id_fa4b618c_fk_Product_Product_id` FOREIGN KEY (`Product_id_id`) REFERENCES `product` (`Product_id`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `Product_Category_id_id_94e10cf3_fk_Category_Category_id` FOREIGN KEY (`Category_id_id`) REFERENCES `category` (`Category_id`);

--
-- Constraints for table `table_booking`
--
ALTER TABLE `table_booking`
  ADD CONSTRAINT `Table_booking_Customer_id_id_9a2e449e_fk_Customer_Customer_id` FOREIGN KEY (`Customer_id_id`) REFERENCES `customer` (`Customer_id`),
  ADD CONSTRAINT `Table_booking_Table_id_id_aa5d4ee6_fk_Cafe_Table_Table_id` FOREIGN KEY (`Table_id_id`) REFERENCES `cafe_table` (`Table_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
