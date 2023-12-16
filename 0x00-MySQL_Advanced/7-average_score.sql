-- Task: Create a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student

-- Create the stored procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the average score for the student
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the average score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = p_user_id;
END $$
DELIMITER ;
