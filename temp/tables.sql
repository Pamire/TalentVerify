CREATE TABLE IF NOT EXISTS company (
	company_id INTEGER PRIMARY KEY NOT NULL,
	"name" TEXT NOT NULL,
	registration_number TEXT NOT NULL,
	address TEXT NULL,
	contact_person_name TEXT NULL,
	contact_person_email TEXT NULL,
	contact_person_phone_number TEXT NULL
);

CREATE TABLE IF NOT EXISTS department (
	"name" TEXT NOT NULL,
	department_id INTEGER PRIMARY KEY NOT NULL,
	company_id INTEGER NOT NULL,
	CONSTRAINT department_fk FOREIGN KEY (company_id) REFERENCES company(company_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS employee (
	employee_id TEXT NULL,
	person_id INTEGER PRIMARY KEY NOT NULL,
	email TEXT NULL,
	phone_number TEXT NULL,
	date_started TEXT NOT NULL,
	date_left TEXT NULL,
	duties TEXT NULL, -- split by specified delimeter to get list of duties
	company_id INTEGER NOT NULL,
	department_id INTEGER NOT NULL,
	CONSTRAINT employee_fk FOREIGN KEY (company_id) REFERENCES company(company_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT employee_fk_1 FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE ON UPDATE CASCADE
);


insert into company (name, registration_number) values ('FIRST MUTUAL', 'CO-12-567');