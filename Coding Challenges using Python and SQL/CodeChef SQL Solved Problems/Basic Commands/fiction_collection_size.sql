 -- Basic Commands: Fiction Collection Size

SELECT
    COUNT(id) AS fiction_count
FROM
    Books
WHERE
    genre = 'Fiction';
