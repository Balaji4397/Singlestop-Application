CREATE TABLE if not exists SHIPPING_STATUS(
ship_id	INT PRIMARY KEY NOT NULL,
ship_date DATE,
ship_track_no BIGINT,
order_id INT,
invoice_num INT);


