ALTER TABLE PRODUCT_STOCK_DETAILS
ADD FOREIGN KEY (seller_id) references SELLER_DETAILS (seller_id);
