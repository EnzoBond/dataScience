create table purchase(purchase_id serial primary key,
                      total_price decimal(10,2) not null,
                      purchase_date timestamp,
                      shipped_date timestamp,
                      ship_address varchar(60),
                      ship_city varchar(15),
                      ship_country varchar(15));

create table customer(customer_id serial primary key,
                      contact_name varchar(30) not null ,
                      company_name varchar(30),
                      contact_email varchar(128) not null,
                      address varchar(120),
                      city varchar(30),
                      country varchar(30));

create table employee(employee_id serial primary key,
                      first_name varchar(20) not null,
                      last_name varchar(40) not null,
                      birth_date date,
                      hire_date date,
                      address varchar(128),
                      city varchar(30),
                      country varchar(30),
                      reports_to int references employee(employee_id));

create table product(product_id serial primary key,
                     product_name varchar(40) not null,
                     quantity_per_unit int,
                     unit_price decimal(10,2),
                     units_in_stock int,
                     discontinued boolean);

create table category(category_id serial primary key,
                      name varchar(60) not null ,
                      description text,
                      parent_category_id int references category(category_id));

create table purchase_item(purchase_id int references purchase(purchase_id),
                           product_id int references product(product_id),
                           unit_price decimal(10,2) not null,
                           quantity int not null,
                           primary key (purchase_id, product_id));


--Relações da tabela "purchase"
alter table purchase -- Relação entre "purchase" e "customer"
    add column customer_id int,
    add constraint fk_purchase_customer foreign key (customer_id) references customer(customer_id);

alter table purchase -- Relação entre "purchase" e "employee"
    add column employee_id int,
    add constraint fk_purchase_employee foreign key (employee_id) references employee(employee_id);

--Relações da tabela "product"
alter table product -- Relação entre "product" e "category"
   add column category_id int,
   add constraint fk_product_category foreign key (category_id) references category(category_id);