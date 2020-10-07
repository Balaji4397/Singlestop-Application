CREATE TABLE if not exists CUSTOMER_ADDRESS_DETAILS(
address_id int PRIMARY KEY NOT NULL,
address_1 varchar(25),
address_2 varchar(25),
state varchar(20),
country varchar(20),
address_type varchar(15),
pin_code bigint not null,
customer_id int);

