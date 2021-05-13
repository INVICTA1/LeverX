USE rooms;

DROP PROCEDURE IF EXISTS usp_find_list_rooms_with_students;
DELIMITER $$
CREATE PROCEDURE usp_find_list_rooms_with_students()
	BEGIN
		SELECT 	r.`name`,
				count(r.id) as num_students
		FROM rooms r
		JOIN students s
		ON r.id = s.room
		GROUP BY r.id;
    END
$$
DELIMITER ;
