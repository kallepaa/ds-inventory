-- SQLite
CREATE TABLE IF NOT EXISTS inventory (
	id integer PRIMARY KEY,
	product_name text NOT NULL,
	price decimal,    
	balance int
);

CREATE TABLE IF NOT EXISTS reservation (
	id integer PRIMARY KEY,
	reserved int,
    inventory_id int,
	order_id text NOT NULL,
    FOREIGN KEY (inventory_id) REFERENCES inventory (id)    
);
