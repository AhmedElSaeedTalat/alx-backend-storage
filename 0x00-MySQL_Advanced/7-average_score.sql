-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SET @AV = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
	UPDATE users SET average_score = @AV WHERE id = user_id;
END;
|
DELIMITER ;
