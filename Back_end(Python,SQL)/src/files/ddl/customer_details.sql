CREATE TABLE if not exists CUSTOMER_DETAILS(
customer_id int PRIMARY KEY NOT NULL ,
customer_name varchar(15) NOT NULL,
customer_ph_no bigint,
customer_type varchar(10) DEFAULT 'GEN',
customer_mail_id varchar(25) NOT NULL,
customer_pass varchar(12) NOT NULL,
customer_gen varchar(10));
