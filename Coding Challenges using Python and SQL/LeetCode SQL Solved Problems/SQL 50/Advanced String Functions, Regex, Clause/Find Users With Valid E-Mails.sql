-- 1517. Find Users With Valid E-Mails
-- Categories : Database

SELECT *
FROM
    Users
WHERE
    mail REGEXP '^[A-Za-z][A-Za-z0-9\\_\\.\\-]*@leetcode\\.com$';
