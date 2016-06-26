select * from district;
drop table district;
show variables like '%char%';
set names 'utf8';

create table district
(
    id int auto_increment not null,
    area float,
    distName varchar(50),
    population float,
    primary key(id)
) DEFAULT CHARSET=utf8;

create table skitrack
(
	id int auto_increment not null,
    distid int,
    address varchar(100),
	phonenumber int,
    flagwc boolean,
    flagrent boolean,
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;


create table market
(
	id int auto_increment not null,
    distid int,
    address varchar(100),
    phonenumber int,
    kind varchar(50),
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

create table park
(
	id int auto_increment not null,
    distid int,
    address varchar(100),
    flagwater boolean,
    flagchildarea boolean,
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

create table wifispot
(
	id int auto_increment not null,
    distid int,
    skitrackid int,
    spotname varchar(50),
    zone int,
    privacy varchar(50),
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade,
	foreign key(skitrackid) references skitrack(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

create table eduplace
(
	id int auto_increment not null,
    distid int,
    address varchar(100),
    phonenumber int,
    placetype varchar(50),
    form varchar(50),
    head varchar(50),
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

create table bar
(
	id int auto_increment not null,
    distid int,
    address varchar(50),
    phonenumber int,
    sitsnum int,
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

create table fracture
(
	id int auto_increment not null,
    distid int,
    barid int,
    address varchar(100),
    phonenumber int,
    head varchar(50),
    lattitude float,
    longitude float,
    primary key(id),
    foreign key(distid) references district(id)
		on update cascade
        on delete cascade,
	foreign key(barid) references district(id)
		on update cascade
        on delete cascade
) DEFAULT CHARSET=utf8;

select * from district;