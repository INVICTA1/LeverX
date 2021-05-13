USE rooms;

CREATE TABLE students(id 		INT,
					birthday 	DATE NOT NULL,
					`name` 	VARCHAR(200),
					room	INT,
					sex 	CHAR,
					CONSTRAINT pk_students PRIMARY KEY(id),
                    CONSTRAINT fk_sudents_rooms FOREIGN KEY (room) REFERENCES rooms(id) ON DELETE CASCADE ON UPDATE CASCADE);