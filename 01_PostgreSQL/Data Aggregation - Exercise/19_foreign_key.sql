CREATE TABLE employees_projects (
    id SERIAL PRIMARY KEY,
    employee_id INT,
    project_id INT,
	FOREIGN KEY (employee_id) REFERENCES employees(id),
	FOREIGN KEY (project_id) REFERENCES projects(id)
);


-- CREATE TABLE employees_projects (
--     id SERIAL PRIMARY KEY,
--     employee_id INT,
--     project_id INT,
--     CONSTRAINT fk_employee_id FOREIGN KEY (employee_id) REFERENCES employees(id),
--     CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES projects(id)
-- );
