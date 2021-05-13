USE rooms;

DROP PROCEDURE IF EXISTS usp_top5_rooms_with_diff_age;
DELIMITER $$
CREATE PROCEDURE usp_top5_rooms_with_diff_age()
	BEGIN
		SELECT r.`name`
		FROM rooms r
		JOIN (SELECT room,
					(max(birthday) - min(birthday)) as diff_birth
					FROM students
					GROUP BY room
					ORDER BY diff_birth DESC
					LIMIT 5) diff_birth
		ON r.id = diff_birth.room;
    END
$$
DELIMITER ;
