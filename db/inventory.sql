DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS brands;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255),
    carraige_paid INT
);

CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL 
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    in_stock INT,
    low_stock_threshold INT,
    buying_price INT,
    selling_price INT,
    supplier_id INT REFERENCES suppliers(id) ON DELETE CASCADE,
    brand_id INT REFERENCES brands(id) ON DELETE CASCADE
);

