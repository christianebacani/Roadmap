-- Question: For each day display the total amount of admissions on that day. Display the amount changed from the previous date.
-- Categories: Hard

SELECT
    admission_date,
    COUNT(*) AS admission_day,
    COUNT(*) - LAG(COUNT(*), 1, NULL) OVER (ORDER BY admission_date ASC) AS admission_count_change
FROM
    admissions
GROUP BY
    admission_date;
