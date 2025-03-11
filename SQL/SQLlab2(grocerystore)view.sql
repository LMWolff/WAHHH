SELECT
ItemName,
Quanity,
Sold AS 'Amount Sold',
costperitem AS 'Price',
TypeofFood,
ROUND(Sold * costperitem ,2) AS 'Total Dollar Amout of Sales'
from Store s 
