CREATE TABLE illinois_transformed(
	Date DATE NOT NULL,
	Illinois_Precip FLOAT NOT NULL,
	Illinois_Temp FLOAT NOT NULL,
	PRIMARY KEY (Date)
);


CREATE TABLE iowa_transformed(
	Date DATE NOT NULL,
	Iowa_Precip FLOAT NOT NULL,
	Iowa_Temp FLOAT NOT NULL,
	PRIMARY KEY (Date)
);	


CREATE TABLE soybean_transformed(
	Date DATE NOT NULL,
	Soybean_Open_Price FLOAT NOT NULL,
	Soybean_Avg_Price FLOAT NOT NULL,
	PRIMARY KEY (Date)
);	


CREATE TABLE crude_oil_transformed(
	Date DATE NOT NULL,
	Crude_Open_Price FLOAT NOT NULL,
	Crude_Avg_Price FLOAT NOT NULL,
	PRIMARY KEY (Date)
);		

	