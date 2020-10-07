CREATE TABLE if not exists ORDER_DETAILS(
order_id INT PRIMARY KEY NOT NULL,
order_date DATE,
billing_name VARCHAR(10),
delivery_name VARCHAR(10),
billing_address_id int,
delivery_address_id int,
order_status_id	int,
customer_id int,
FOREIGN KEY (billing_address_id) REFERENCES CUSTOMER_ADDRESS_DETAILS (address_id),
FOREIGN KEY (delivery_address_id) REFERENCES CUSTOMER_ADDRESS_DETAILS (address_id),
FOREIGN KEY (order_status_id) REFERENCES ORDER_STATUS_DETAILS (order_status_id),
FOREIGN KEY (customer_id) REFERENCES CUSTOMER_DETAILS (customer_id));

