CREATE DATABASE aula22;

go 

USE aula22;

go

CREATE TABLE cat (
	id int primary key identity(1,1),
	name varchar(50),
	breed varchar(50),
	age int,
	sex CHAR DEFAULT 'M' CHECK(sex IN ('M', 'F')),
	fav_toy varchar(50),
	coloration varchar(50)
)

GO

INSERT INTO cat (name, breed, age, sex, fav_toy, coloration) VALUES 
('Gato de Botas', 'Siamês', 2, 'M', 'Brinquedo de Rato', 'Cinza'),
('Morgana', 'Bengal', 3, 'F', 'Varinha com Pena', 'Marrom'),
('Cacau', 'Viralata', 1, 'M', 'Novelo de Lã', 'Laranja'),
('Yuumi', 'Persa', 4, 'M', 'Ponteiro Laser', 'Branco'),
('Tigrão', 'Maine Coon', 5, 'F', 'Brinquedo de Catnip', 'Preto')

GO

UPDATE cat 
SET name = 'VELHA TURBO' 
WHERE ID = 3

GO

SELECT name, breed, coloration FROM cat 
WHERE age >= 2 ORDER BY name DESC

GO

SELECT * FROM cat 
WHERE breed LIKE 'M%' 
AND fav_toy LIKE 'B%' 
AND coloration LIKE '%A'

GO

UPDATE cat 
SET coloration = 'Cinza' 
WHERE ID = 5

GO

SELECT * FROM cat

INSERT INTO cat (name, breed, age, sex, coloration) VALUES
('Thiaguinho', 'Viralata', 45, 'F', 'Preto'),
('Pedrão', 'Viralata', 70, 'M', 'Cinza')

SELECT * FROM cat WHERE sex = 'M' AND fav_toy IS NULL
 
DELETE cat WHERE id = 8

SELECT name FROM cat 
ORDER BY age DESC

SELECT coloration, COUNT (*) AS numbers_cats 
FROM cat 
GROUP BY coloration 
ORDER BY numbers_cats ASC

SELECT breed, age, AVG (age) AS avg_age_cats 
FROM cat 
GROUP BY breed, age 
ORDER BY avg_age_cats ASC

SELECT breed, AVG(age) OVER(PARTITION BY breed) AS avg_age_cats,  COUNT(breed) OVER(PARTITION BY breed) AS count_breed_cats
FROM cat
GROUP BY breed, age
HAVING COUNT(age) > 1 ORDER BY age DESC


