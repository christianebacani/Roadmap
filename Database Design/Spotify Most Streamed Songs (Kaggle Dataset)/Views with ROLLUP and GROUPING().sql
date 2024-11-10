-- Database name
USE practicedb;


-- Creating views (Virtual Table) using also ROLLUP and GROUPING() Function


-- Create view
CREATE VIEW grand_or_sub_total_streams AS 
SELECT
	spotify_most_streamed_songs.spotify_tracking_id,
    FORMAT(SUM(streams), 0) AS total_streams,
    GROUPING(spotify_most_streamed_songs.spotify_tracking_id) AS is_grand_total
FROM 
	spotify_most_streamed_songs
INNER JOIN
	spotify_trackings
USING(spotify_tracking_id)
GROUP BY
	spotify_most_streamed_songs.spotify_tracking_id WITH ROLLUP
ORDER BY 
    is_grand_total DESC, 
    total_streams ASC;
    

-- Create view
CREATE VIEW songs_releases_streams AS
SELECT
	track_name,
    artist_id,
    FORMAT(streams, 0) AS streams,
    spotify_tracking_id,
    apple_tracking_id,
    deezer_tracking_id,
    shazam_tracking_id,
	CONCAT(released_year, '-', released_month, '-', released_day) AS release_date
FROM 
	spotify_most_streamed_songs
INNER JOIN
	spotify_song_release_dates
USING(date_id)
INNER JOIN
	spotify_trackings
USING(spotify_tracking_id)
ORDER BY
	release_date DESC;
    

    















    
    

    



    
    

    
    
    
    


    



    
