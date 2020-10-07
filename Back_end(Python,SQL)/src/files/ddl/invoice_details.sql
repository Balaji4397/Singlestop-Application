CREATE TABLE if not exists INVOICE_DETAILS(
invoice_num INT PRIMARY KEY ,
invoice_date DATE,
invoice_desc VARCHAR(30),
order_id INT,
product_id INT);

