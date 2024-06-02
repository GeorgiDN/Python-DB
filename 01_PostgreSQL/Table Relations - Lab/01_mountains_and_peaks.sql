CREATE TABLE mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	mountain_id INT,
	CONSTRAINT fk_peaks_mountains 
		FOREIGN KEY (mountain_id) 
			REFERENCES Mountains(id)
);