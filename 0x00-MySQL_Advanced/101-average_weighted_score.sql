-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score *
                                    projects.weight) / SUM(projects.weight)
                         FROM corrections, projects
                         WHERE corrections.user_id = users.id AND 
                         projects.id = corrections.project_id)
    where id = users.id;
END $$
DELIMITER ;
