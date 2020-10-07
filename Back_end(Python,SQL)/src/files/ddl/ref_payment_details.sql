ALTER TABLE PAYMENT_DETAILS
ADD FOREIGN KEY (order_id) REFERENCES ORDER_DETAILS (order_id),
ADD FOREIGN KEY (product_id) REFERENCES PRODUCT_DETAILS (product_id),
ADD FOREIGN KEY (customer_id) REFERENCES CUSTOMER_DETAILS (customer_id);