# Question: Radio DJ helper function
# Categories: 7 Kyu

def longest_possible(playback: int) -> str | bool:
    songs = [
        {'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, 
        {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, 
        {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, 
        {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, 
        {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, 
        {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, 
        {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, 
        {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, 
        {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}
        ]
    
    qualified_songs = []

    for i in range(len(songs)):
        song_length = songs[i]['playback']
        minutes = int(song_length.split(':')[0])
        seconds = int(song_length.split(':')[1])
        total_seconds = (minutes * 60) + seconds

        if total_seconds <= playback:
            qualified_songs.append(songs[i])

    maximum_song_length = 0

    for i in range(len(qualified_songs)):
        song_length = qualified_songs[i]['playback']
        minutes = int(song_length.split(':')[0])
        seconds = int(song_length.split(':')[1])
        total_seconds = (minutes * 60) + seconds

        if total_seconds >= maximum_song_length:
            maximum_song_length = total_seconds

    for i in range(len(qualified_songs)):
        song_length = qualified_songs[i]['playback']
        minutes = int(song_length.split(':')[0])
        seconds = int(song_length.split(':')[1])
        total_seconds = (minutes * 60) + seconds

        if maximum_song_length == total_seconds:
            return qualified_songs[i]['title']

    return False