ALTER TABLE SHIPPING_STATUS
ADD FOREIGN KEY (order_id) REFERENCES ORDER_DETAILS (order_id),
ADD FOREIGN KEY (invoice_num) REFERENCES INVOICE_DETAILS (invoice_num);


