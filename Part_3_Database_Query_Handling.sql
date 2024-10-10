CREATE DATABASE OnlineBookstore;

use OnlineBookstore;

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE OrderDetails (
    order_id INT,
    book_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, book_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Insert Customers
INSERT INTO Customers (name, email) VALUES 
('Alice Smith', 'alice@example.com'),
('Bob Johnson', 'bob@example.com'),
('Carol Williams', 'carol@example.com'),
('David Brown', 'david@example.com');

-- Insert Books
INSERT INTO Books (title, author, price) VALUES 
('Book One', 'Author A', 19.99),
('Book Two', 'Author B', 29.99),
('Book Three', 'Author A', 9.99),
('Book Four', 'Author C', 14.99),
('Book Five', 'Author B', 24.99);

-- Insert Orders
INSERT INTO Orders (customer_id, order_date) VALUES 
(1, '2024-01-01 10:00:00'),
(1, '2024-01-05 12:30:00'),
(2, '2024-01-06 09:00:00'),
(3, '2024-01-07 11:00:00'),
(4, '2024-01-08 10:30:00');

-- Insert OrderDetails to create quantities over 10 for some books
INSERT INTO OrderDetails (order_id, book_id, quantity) VALUES 
(1, 1, 4),  -- 4 copies of Book One
(1, 2, 3),  -- 3 copies of Book Two
(2, 1, 2),  -- 2 copies of Book One
(2, 3, 1),  -- 1 copy of Book Three
(3, 1, 5),  -- 5 copies of Book One (total 14 for Book One)
(3, 2, 1),  -- 1 copy of Book Two
(4, 1, 1),  -- 1 copy of Book One
(4, 4, 2),  -- 2 copies of Book Four
(5, 2, 1);  -- 1 copy of Book Two

SELECT 'Top 5 Customers:' AS message;
SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.customer_id, c.name
ORDER BY total_books DESC
LIMIT 5;


SELECT 'Total Revenue Generated from Book Sales by Each Author:' AS message;
SELECT b.author, SUM(b.price * od.quantity) AS total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
JOIN Orders o ON od.order_id = o.order_id
GROUP BY b.author;


SELECT 'Books That Have Been Ordered More Than 10 Times:' AS message;
SELECT b.book_id, b.title, SUM(od.quantity) AS total_ordered
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.book_id, b.title
HAVING total_ordered > 10;
