-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser (user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score)
                         FROM corrections
                         WHERE user_id = user_id)
    where id = user_id;
END $$
DELIMITER ;
