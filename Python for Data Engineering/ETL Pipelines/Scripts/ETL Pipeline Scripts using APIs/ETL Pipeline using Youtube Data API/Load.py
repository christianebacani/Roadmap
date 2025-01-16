# Load

def load(mostPopularYoutubeVideosData):
    targetFilepath = 'Target Data Files\\Most Popular Youtube Videos Data in Philippines\\most_popular_youtube_videos_data.csv'
    mostPopularYoutubeVideosData.to_csv(targetFilepath, index=False)

    return mostPopularYoutubeVideosData

