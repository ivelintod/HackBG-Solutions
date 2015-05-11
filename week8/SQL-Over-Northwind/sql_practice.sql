SELECT ContactName, ContactTitle FROM customers

SELECT * FROM employees WHERE City = 'Seattle'

SELECT * FROM employees WHERE City = 'London'

SELECT * FROM employees WHERE Title LIKE '%Sales%'

SELECT * FROM employees WHERE Title LIKE '%Sales%' AND (TitleOfCourtesy = 'Ms.'
or TitleOfCourtesy = 'Mrs.')

SELECT * FROM employees
ORDER BY BirthDate DESC
LIMIT 5

SELECT * FROM employees
ORDER BY HireDate ASC
LIMIT 5

SELECT EmployeeID, FirstName, LastName, ReportsTo FROM employees
WHERE EmployeeID = 2

SELECT e1.FirstName, e1.LastName, e2.FirstName, e2.LastName
FROM employees AS e1
LEFT JOIN employees AS e2
ON e1.ReportsTo = e2.EmployeeID

SELECT COUNT(TitleOfCourtesy) as count_female FROM employees
WHERE TitleOfCourtesy = 'Ms.' or TitleOfCourtesy = 'Mrs.'

SELECT COUNT(TitleOfCourtesy) as count_male FROM employees
WHERE TitleOfCourtesy = 'Mr.'

SELECT City, COUNT(City) as count_cities FROM employees
GROUP BY City

SELECT OrderID, FirstName, LastName
FROM orders
LEFT JOIN employees
ON orders.EmployeeID = employees.EmployeeID
ORDER BY FirstName

SELECT OrderID, CompanyName
FROM orders
LEFT JOIN shippers
ON orders.ShipVia = shippers.ShipperID
ORDER BY CompanyName

SELECT ShipCountry, COUNT(ShipCountry)
FROM orders
GROUP BY ShipCountry

SELECT EmployeeID, COUNT(EmployeeID) as max_order
FROM orders
GROUP BY EmployeeID
ORDER BY max_order DESC
LIMIT 1

SELECT CustomerID, COUNT(CustomerID) as max_placed_orders
FROM orders
GROUP BY CustomerID
ORDER BY max_placed_orders DESC
LIMIT 1

SELECT o.OrderID, e.FirstName, e.LastName, c.ContactName
FROM employees as e, customers as c, orders as o
ON c.CustomerID = o.CustomerID and e.EmployeeID = o.EmployeeID

SELECT c.ContactName, s.CompanyName
FROM customers as c, orders as o, shippers as s
WHERE c.CustomerID = o.CustomerID  AND o.ShipVia = s.ShipperID
ORDER BY ContactName
