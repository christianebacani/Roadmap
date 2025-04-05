-- Question: Duplicate Emails
-- Categories: Easy

WITH
    number_of_emails AS (
SELECT
    Email,
    COUNT(*) AS Email_Count
FROM
    Person
GROUP BY
    Email
    )

SELECT
    number_of_emails.Email
FROM
    number_of_emails
WHERE
    number_of_emails.Email_Count > 1;
