ALTER TABLE CATEGORY_PRODUCT_DETAILS
ADD FOREIGN KEY (product_id) REFERENCES PRODUCT_DETAILS (product_id),
ADD FOREIGN KEY (category_id) REFERENCES CATEGORY_DETAILS (category_id);

