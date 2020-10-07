CREATE TABLE if not exists CUSTOMER_RATING_DETAILS(
rating_id INT PRIMARY KEY NOT NULL,
rating_star DOUBLE,
rating_desc VARCHAR(50),
customer_id INT,
product_id INT);

