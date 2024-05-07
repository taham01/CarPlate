CREATE DATABASE carDatabase; 
USE CarDatabase;
CREATE TABLE Cars (
    PlateNumber VARCHAR(20) PRIMARY KEY,
    CarMake VARCHAR(50),
    OwnerPhoneNumber VARCHAR(15),
    OwnerName VARCHAR(100)
);

INSERT INTO Cars (PlateNumber, CarMake, OwnerPhoneNumber, OwnerName)
VALUES
    ('ABC123', 'Toyota', '123-456-7890', 'John Doe'),
    ('XYZ456', 'Mercedes', '987-654-3210', 'Jane Smith');

SELECT * FROM Cars;
