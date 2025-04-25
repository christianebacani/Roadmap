-- Question: Ad-Free Sessions
-- Categories: Moderate

WITH
    session_and_num_ads AS (
SELECT
    session_id,
    customer_id,
    start_time,
    end_time,
    (SELECT COUNT(ad_id) FROM Ads WHERE Ads.customer_id = Playback.customer_id AND Ads.timestamp BETWEEN Playback.start_time AND Playback.end_time) AS number_of_ads_appeared
FROM
    Playback)


SELECT
    session_id
FROM
    session_and_num_ads
WHERE
    number_of_ads_appeared = 0;

