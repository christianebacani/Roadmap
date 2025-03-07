-- Basic Commands: Handling NULL Values

SELECT
    book_id,
    title,
    author,
    published_year
FROM
    Library
WHERE
    rating IS NULL;
