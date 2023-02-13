CREATE TABLE IF NOT EXISTS users (
	id serial PRIMARY KEY NOT NULL,
	email varchar(100) NOT NULL,
	password varchar(200) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
	id serial PRIMARY KEY NOT NULL,
	name varchar(100) UNIQUE NOT NULL,
	price float NOT NULL,
	score bigint NOT null,
	image varchar(200) not null
);

CREATE TYPE sale_status AS ENUM ('PENDING', 'COMPLETE');

CREATE TABLE IF NOT EXISTS sales (
	id serial PRIMARY KEY NOT NULL,
	sale_date date NOT NULL,
	status sale_status not null,
	sale_total float not null,
	id_user integer NOT NULL,
	id_game integer NOT NULL,
	CONSTRAINT sale_user FOREIGN KEY (id_user) REFERENCES users(id),
	CONSTRAINT sale_game FOREIGN KEY (id_game) REFERENCES games(id)
);

insert into 
	games (name, price, score, image) 
values 
	('Super Mario Odyssey', 197.88, 100, './assets/super-mario-odyssey.png'),
	('Call Of Duty Infinite Warfare', 49.99, 80, './assets/call-of-duty-infinite-warfare.png'),
	('The Witcher III Wild Hunt', 119.5, 250, './assets/the-witcher-iii-wild-hunt.png'),
	('Call Of Duty WWII', 249.99, 205, './assets/call-of-duty-wwii.png'),
	('Mortal Kombat XL', 69.99, 150, './assets/mortal-kombat-xl.png'),
	('Shards of Darkness', 71.94, 400, './assets/shards-of-darkness.png'),
	('Terra MÃ©dia: Sombras de Mordor', 79.99, 50, './assets/terra-media-sombras-de-mordor.png'),
	('FIFA 18', 195.39, 325, './assets/fifa-18.png'),
	('Horizon Zero Dawn', 115.8, 290, './assets/horizon-zero-dawn.png');
	
insert into users(email, password) values ('teste@teste.com', '123456');