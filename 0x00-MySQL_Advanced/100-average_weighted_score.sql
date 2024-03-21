-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (userId INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score *
                                    projects.weight) / SUM(projects.weight)
                         FROM corrections, projects
                         WHERE corrections.user_id = userId AND 
                         projects.id = corrections.project_id)
    where id = userId;
END $$
DELIMITER ;
