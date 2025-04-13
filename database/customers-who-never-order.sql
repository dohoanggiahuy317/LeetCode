# Write your MySQL query statement below
SELECT Customers.name as Customers
FROM Customers
LEFT JOIN Orders
ON Orders.customerId=Customers.id
WHERE Orders.customerId IS NULL;