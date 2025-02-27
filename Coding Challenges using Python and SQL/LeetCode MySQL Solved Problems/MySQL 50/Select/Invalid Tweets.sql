-- 1683. Invalid Tweets
-- Category : Database
 
SELECT
    tweet_id
FROM
    Tweets
WHERE
    LENGTH(content) > 15;
