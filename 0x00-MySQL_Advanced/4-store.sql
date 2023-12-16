-- Task: Create a trigger to decrease the quantity of an item after adding a new order

-- Create the trigger
CREATE TRIGGER decrease_quantity_trigger
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
