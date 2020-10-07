CREATE TABLE if not exists ORDER_DETAILS(
order_id INT PRIMARY KEY NOT NULL,
order_date DATE,
billing_name VARCHAR(10),
delivery_name VARCHAR(10),
billing_address_id int,
delivery_address_id int,
order_status_id	int,
customer_id int);

