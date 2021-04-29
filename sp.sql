
GO;
CREATE PROCEDURE uspInsertUser @name,@email 
AS
INSERT INTO Students (name,email) VALUES (@name, @email);
GO;
