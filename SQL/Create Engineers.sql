drop table user_steam_games;
drop table user_steam_recommended_games_buy;
drop table user_steam_recommended_games_play;
drop table steam_games;
drop table users;


create table steam_games(
appid int primary key,
title varchar(100) not null,
has_achievements bool not null,
genre varchar(25) default "Empty"
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

create table user_steam_recommended_games(
id int primary key auto_increment,
user_id int not null,
game_id int not null,
type varchar(20) not null,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (game_id) REFERENCES steam_games(appid)
);
