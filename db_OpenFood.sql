CREATE DATABASE OpenFood ;


CREATE TABLE category(
category_id int unsigned AUTO_INCREMENT ,
category_name varchar(40),

PRIMARY KEY(category_id)

)ENGINE = InnoDB;

CREATE TABLE products(

category_id INTEGER UNSIGNED NOT NULL,
product_name VARCHAR(90) NOT NULL,
nutrition_score INTEGER NOT NULL,
product_id INTEGER UNSIGNED AUTO_INCREMENT,
url VARCHAR(200) NOT NULL,
store VARCHAR(200),




PRIMARY KEY (product_id, product_name),
UNIQUE (product_id, product_name),
FOREIGN KEY (category_id)
REFERENCES category (category_id)



)ENGINE = InnoDB;


CREATE TABLE favorites (

category_id INTEGER UNSIGNED NOT NULL,
product_name VARCHAR(90) NOT NULL,
product_id INTEGER UNSIGNED AUTO_INCREMENT,
url VARCHAR(200) NOT NULL,
store VARCHAR(200),




PRIMARY KEY (product_id, product_name),
UNIQUE (product_id, product_name),
FOREIGN KEY (category_id)
REFERENCES category (category_id)


)
ENGINE = InnoDB;


INSERT INTO category (category_name) VALUES ('Aliments et boissons à base de végétaux'),
('Aliments d''origine végétale'),('Snacks'),('Boissons'),('Snacks sucrés');
