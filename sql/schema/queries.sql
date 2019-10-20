
SELECT soybean.date, soybean.soybean_avg_price,crude_oil.crude_avg_price,iowa.iowa_temp, illinois.illinois_temp
FROM crude_oil
INNER JOIN soybean
ON crude_oil.date = soybean.date
INNER JOIN illinois
ON illinois.date = soybean.date
INNER JOIN iowa
ON iowa.date = soybean.date;

-- Create view from query
go

CREATE VIEW joined_tables AS
SELECT s.date, s.soybean_avg_price, c.crude_avg_price,i.iowa_temp, l.illinois_temp
FROM crude_oil AS c
INNER JOIN soybean AS s
ON (c.date = s.date)
INNER JOIN illinois AS l
ON (l.date = s.date)
INNER JOIN iowa AS i
ON (i.date = s.date);

go 
    


-- Query the table view created
SELECT *
FROM joined_tables;

-- Effect of tarrifs on avergae soybean price, see avg price before 2019 and in 2019
SELECT AVG(soybean_avg_price) FROM joined_tables;
SELECT AVG(soybean_avg_price) FROM joined_tables
Where date < '2019-01-01';
SELECT AVG(soybean_avg_price) FROM joined_tables
Where date >= '2019-01-01' ;

-- Drop view
-- DROP VIEW joined_tables;
