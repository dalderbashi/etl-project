CREATE TABLE illinois(
	date DATE NOT NULL,
	illinois_precip FLOAT NOT NULL,
	illinois_temp FLOAT NOT NULL,
	PRIMARY KEY (date)
);


CREATE TABLE iowa(
	date DATE NOT NULL,
	iowa_precip FLOAT NOT NULL,
	iowa_temp FLOAT NOT NULL,
	PRIMARY KEY (date)
);	


CREATE TABLE soybean(
	date DATE NOT NULL,
	soybean_open_price FLOAT NOT NULL,
	soybean_avg_price FLOAT NOT NULL,
	PRIMARY KEY (date)
);	


CREATE TABLE crude_oil(
	date DATE NOT NULL,
	crude_open_price FLOAT NOT NULL,
	crude_avg_price FLOAT NOT NULL,
	PRIMARY KEY (date)
);
