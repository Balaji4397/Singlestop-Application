CREATE TABLE if not exists PRODUCT_ORDERED_DETAILS(
ordered_product_id INT PRIMARY KEY NOT NULL,
ordered_quantity INT,
ordered_date DATE,
order_id INT,
product_id INT);

