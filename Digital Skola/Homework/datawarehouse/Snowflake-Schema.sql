-- Create Schema
CREATE SCHEMA IF NOT EXISTS "E-Commerce" AUTHORIZATION learning;
ALTER SCHEMA "E-Commerce" RENAME TO Storepedia owner to learning;

-- Fact Table
-- Table: Orders
CREATE TABLE storepedia.orders (
    OrderID SERIAL PRIMARY KEY,
    OrderUserID INT,
    OrderAmount FLOAT,
    OrderShipName VARCHAR(100),
    OrderShipAddress1 VARCHAR(100),
    OrderShipAddress2 VARCHAR(100),
    OrderCity VARCHAR(50),
    OrderState VARCHAR(50),
    OrderZip VARCHAR(20),
    OrderCountry VARCHAR(50),
    OrderPhone VARCHAR(20),
    OrderFax VARCHAR(20),
    OrderEmail VARCHAR(100),
    OrderDate TIMESTAMP,
    OrderShipped SMALLINT,
    OrderTrackingNumber VARCHAR(80)
);

-- Dimensional:
-- Dim Table: Order Details
CREATE TABLE storepedia.orderdetails (
    DetailID SERIAL PRIMARY KEY,
    DetailOrderID INT,
    DetailProductID INT,
    DetailName VARCHAR(250),
    DetailPrice FLOAT,
    DetailSKU VARCHAR(50),
    DetailQty INT
);

-- Dim Table: User
CREATE TABLE storepedia.users (
    UserID SERIAL PRIMARY KEY,
    UserEmail VARCHAR(500),
    UserPassword VARCHAR(500),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    UserCity VARCHAR(90),
    UserState VARCHAR(20),
    UserZip VARCHAR(12),
    UserEmailVerified BOOLEAN,
    UserRegistrationDate TIMESTAMP,
    UserVerificationCode VARCHAR(20),
    UserIP VARCHAR(50),
    UserPhone VARCHAR(20),
    UserFax VARCHAR(20),
    UserCountry VARCHAR(20),
    UserAddress VARCHAR(100),
    UserAddress2 VARCHAR(50)
);

-- Dim Table: Product
CREATE TABLE storepedia.products (
    ProductID SERIAL PRIMARY KEY,
    ProductSKU VARCHAR(50),
    ProductName VARCHAR(100),
    ProductPrice FLOAT,
    ProductWeight FLOAT,
    ProductCartDesc VARCHAR(250),
    ProductShortDesc VARCHAR(1000),
    ProductLongDesc text,
    ProductThumb VARCHAR(100),
    ProductImage VARCHAR(100),
    ProductCategoryID INT,
    ProductUpdateDate timestamp,
    ProductStock FLOAT,
    ProductLive SMALLINT,
    ProductUnlimited SMALLINT,
    ProductLocation VARCHAR(250)
);

-- Dim Table: Product Categories
CREATE TABLE storepedia.product_categories(
	CategoryID SERIAL PRIMARY KEY,
	CategoryName VARCHAR(50)
);

-- Dim Table: Product Options
CREATE TABLE storepedia.product_options(
	ProductOptionID SERIAL PRIMARY KEY,
	OptionID INT,
	ProductID INT,
	OptionGroupID INT,
	OptionPriceIncrement double precision
);

-- Dim Table: Options
CREATE TABLE storepedia.options(
	OptionID SERIAL PRIMARY KEY,
	OptionName VARCHAR(50)
);

-- Dim Table: Option Groups
CREATE TABLE storepedia.option_groups(
	OptionGroupID SERIAL PRIMARY KEY,
	OptionGroupName VARCHAR(50)
);









