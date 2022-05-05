create database game_library;
use game_library;



drop table user_steam_games;
drop table user_games;
drop table games;
drop table platforms;
drop table ecosystem;
drop table user_steam_recommended_games;
drop table steam_games;
drop table titles;
drop table genres;
drop table users;


create table genres(
id int primary key,
name varchar(25)
);

create table titles(
id int primary key,
name varchar(100),
genre_id int default "0",
FOREIGN KEY (genre_id) REFERENCES genres(id)
);

create table ecosystems(
id int primary key,
name varchar(25)
);

create table platforms(
id int primary key,
ecosystem_id int not null,
name varchar(25),
FOREIGN KEY (ecosystem_id) REFERENCES ecosystems(id)
);

create table steam_games(
appid int primary key,
title_id int not null,
has_achievements bool not null,
genre_id int default "0",
FOREIGN KEY (genre_id) REFERENCES genres(id),
FOREIGN KEY (title_id) REFERENCES titles(id)
);


create table users(
id int primary key auto_increment,
nickname varchar(100) not null unique,
profile_link varchar(100) not null unique,
email varchar(100) not null unique,
hours_played_limit int default 0
);


create table user_steam_games(
id varchar(100) primary key,
user_id int not null,
game_id int not null,
time_played varchar(20),
achievements varchar(10) default "N/A",
achievements_percentage varchar(4) default "0",
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (game_id) REFERENCES steam_games(appid)
);

create table games(
id int primary key,
title_id int not null,
platform_id int not null,
FOREIGN KEY (platform_id) REFERENCES platforms(id)
);

create table user_games(
id int primary key,
user_id int not null,
game_id int not null,
time_played varchar(20),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (game_id) REFERENCES games(id)
);


create table user_steam_recommended_games(
id int primary key auto_increment,
user_id int not null,
game_id int not null,
type varchar(20) not null,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (game_id) REFERENCES steam_games(appid)
);

