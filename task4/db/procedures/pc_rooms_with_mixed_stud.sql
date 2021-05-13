USE rooms;

DROP PROCEDURE IF EXISTS usp_find_list_rooms_with_mixed_students;
DELIMITER $$
CREATE PROCEDURE usp_find_list_rooms_with_mixed_students()
	BEGIN
		SELECT `name`
        FROM rooms
        WHERE id IN (SELECT room
					FROM students
                    WHERE sex = 'F'
                    AND
                    room IN (SELECT room
							FROM students
                            WHERE sex = 'M'));
    END
$$
DELIMITER ;
