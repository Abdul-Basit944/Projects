
USE project_database;

-- Select all records:
SELECT *
FROM `transformed_data`;
 
-- Select the `Market cap(US$ billion)` for `JPMorgan Chase` where the `Rank` is 1.
SELECT `Market cap(US$ billion)`
FROM transformed_data
WHERE `Bank name` = "JPMorgan Chase" AND `Rank` = 1;  

-- Find the bank with the highest market cap in USD:

SELECT `Bank name` 
FROM `transformed_data` 
ORDER BY `Market cap(US$ billion)` DESC LIMIT 1;

-- Find the average market cap in USD:

SELECT AVG(`Market cap(US$ billion)`) 
AS `Average Market Cap (US$ billion)` 
FROM `transformed_data`;

-- Count the number of banks with a market cap in USD greater than 200 billion:

SELECT COUNT(*) 
FROM `transformed_data` 
WHERE `Market cap(US$ billion)` > 200;

-- List all banks with a market cap in EUR greater than 150 billion:

SELECT `Bank name` 
FROM `transformed_data` 
WHERE `Market cap(EUR billion)` > 150;

