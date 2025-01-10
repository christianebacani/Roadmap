import pandas as pd

# Transform

def transform(firstPageMostPopularVideosData, secondPageMostPopularVideosData):
    # Dictionary to store the most popular youtube vides data
    mostPopularYTVideosDict = {'title' : [], 'description' : [], 'channelTitle' : [], 
                               'tags' : [], 'viewCount' : [], 'likeCount' : [], 'commentCount' : []}

    # Combine the two extracted pages of resources containing the most popular youtube videos data
    mostPopularVideosDataList = firstPageMostPopularVideosData + secondPageMostPopularVideosData


    # For loop to get the necessary data and store in the dictionary
    for videoDataDict in mostPopularVideosDataList:
        mostPopularYTVideosDict['title'].append(str(videoDataDict['snippet']['title']).strip())
        descriptions = videoDataDict['snippet']['description']

        if descriptions == '':
            descriptions = 'No Descriptions'
            mostPopularYTVideosDict['description'].append(descriptions)
        
        else:
            mostPopularYTVideosDict['description'].append(descriptions)

        mostPopularYTVideosDict['channelTitle'].append(str(videoDataDict['snippet']['channelTitle']).strip())

        tagsList = videoDataDict['snippet'].get('tags', ['No Tags'])
        tagsList = [str(tags).capitalize().strip() for tags in tagsList]
        tags = ', '.join(tagsList)
        mostPopularYTVideosDict['tags'].append(tags)

        mostPopularYTVideosDict['viewCount'].append(int(str(videoDataDict['statistics']['viewCount']).strip()))
        mostPopularYTVideosDict['likeCount'].append(int(str(videoDataDict['statistics']['likeCount']).strip()))
        mostPopularYTVideosDict['commentCount'].append(int(str(videoDataDict['statistics']['commentCount']).strip()))


    # Convert dictionary to dataframe
    mostPopularYoutubeVideosData = pd.DataFrame(mostPopularYTVideosDict)


    return mostPopularYoutubeVideosData    
