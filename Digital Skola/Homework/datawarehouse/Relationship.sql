-- Users Table and Order Details Table relation with Table Orders
-- Dim Table: Users
ALTER TABLE storepedia.users
ADD CONSTRAINT fk_order_users
FOREIGN KEY (UserID)
REFERENCES storepedia.orders(OrderID);

-- Dim Table: Order Details
ALTER TABLE storepedia.orderdetails 
ADD CONSTRAINT fk_order_detail_users
FOREIGN KEY (DetailID)
REFERENCES storepedia.orders(OrderID);

-- Order Details to relation with Table Products
ALTER TABLE storepedia.orderdetails
ADD CONSTRAINT fk_order_details_products
FOREIGN KEY (DetailID)
REFERENCES storepedia.products(ProductID);

-- Product Options to relation with Table Products
ALTER TABLE storepedia.product_options
ADD CONSTRAINT fk_product_options
FOREIGN KEY (ProductOptionID)
REFERENCES storepedia.products(ProductID);

-- Product Categories to relation with Table Products
ALTER TABLE storepedia.product_categories
ADD CONSTRAINT fk_product_categories
FOREIGN KEY (CategoryID)
REFERENCES storepedia.products(ProductID);

-- Options to relation with Table Products
ALTER TABLE storepedia."options" 
ADD CONSTRAINT fk_options
FOREIGN KEY (OptionID)
REFERENCES storepedia.product_options(ProductOptionID);

-- Options Groups to relation with Table Products
ALTER TABLE storepedia.option_groups 
ADD CONSTRAINT fk_option_groups
FOREIGN KEY (OptionGroupID)
REFERENCES storepedia.product_options(ProductOptionID);

