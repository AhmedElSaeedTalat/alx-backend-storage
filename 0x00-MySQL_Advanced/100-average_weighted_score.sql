-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SET @average = (SELECT AVG(corrections.score * projects.weight) AS average_score
	FROM corrections
	JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id);
	UPDATE users SET average_score = @average
	WHERE users.id = user_id;
END;
|
DELIMITER ;
