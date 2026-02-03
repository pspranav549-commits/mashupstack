CREATE TABLE products(product_id INT NOT NULL AUTO_INCREMENT,product_name TEXT(50)NOT NULL,price INT NOT NULL,PRIMARY KEY(product_id));
INSERT INTO `products`(`product_id`, `product_name`, `price`) VALUES ('1','tv','16999'),('2','mobile','18990'),('3','powerbank','2599');
ALTER TABLE products ADD category TEXT(50);
DROP DATABASE groceryshop_db;