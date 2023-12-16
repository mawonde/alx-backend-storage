- Task: Create a trigger to reset the attribute valid_email only when the email has been changed

-- Create the trigger
CREATE TRIGGER reset_valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = NULL;
    END IF;
END;
