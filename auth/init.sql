CREATE USER 'sqluser'@'localhost' IDENTIFIED BY 'sqluser';

Create database auth;

GRANT ALL PRIVILEGEs ON auth.* TO 'sqluser'@'localhost';

use auth;


create table user(
id int not null auto_increment primary key,
email varchar(255) not null,
password varchar(255) not null

)

Insert into user(email,password) values('haha@gmail.com', 'Admin123')
