-- Question: Spotify Sessions
-- Categories: Easy

WITH
    playback_and_ads AS (
SELECT
    Playback.session_id,
    Playback.customer_id,
    Playback.start_time,
    Playback.end_time,
    Ads.ad_id,
    Ads.customer_id,
    Ads.timestamp
FROM
    Playback
INNER JOIN
    Ads
ON
    Playback.customer_id = Ads.customer_id
    )

SELECT
    DISTINCT
    playback_and_ads.session_id
FROM
    playback_and_ads
WHERE
    playback_and_ads.timestamp NOT BETWEEN playback_and_ads.start_time AND playback_and_ads.end_time
ORDER BY
    playback_and_ads.session_id;
    