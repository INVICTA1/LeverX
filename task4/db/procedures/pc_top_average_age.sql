USE rooms;

DROP PROCEDURE IF EXISTS usp_top5_rooms_with_min_average_age;
DELIMITER $$
CREATE PROCEDURE usp_top5_rooms_with_min_average_age()
	BEGIN
		SELECT r.`name`
        FROM rooms r
        JOIN (	SELECT room,
					 AVG(birthday) AS avg_birth
				FROM students
                GROUP BY room
                ORDER BY avg_birth
                LIMIT 5) avg_birth
		ON r.id = avg_birth.room;
    END
$$
DELIMITER ;
