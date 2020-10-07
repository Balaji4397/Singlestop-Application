CREATE TABLE if not exists PAYMENT_DETAILS(
payment_code INT PRIMARY KEY NOT NULL,
payment_desc VARCHAR(35),
order_id INT,
product_id INT,
customer_id INT);
