create table Store(
ItemName char (20),
Quanity float (5),
Sold float (5),
costperitem float (5),
TypeofFood char (10)
)

Insert into Store
Values
('Apple',15,5,15.00,'Fruit') 
('Banana',20,15,20.00,'Fruit') 
('Ground Beef',5,3,25.00,'Meat') 
('Carrot',10,9,15.00,'Vege3table') 
('Sliced Chicken',6,5,29.99,2) 

ELECT
ItemName,
Quanity,
Sold AS 'Amount Sold',
costperitem AS 'Price',
TypeofFood,
ROUND(Sold * costperitem ,2) AS 'Total Dollar Amout of Sales'
from Store s 
