import sqlite3

# Load

def load(filmsData):
    csvFilepath = 'Target Data Files\\Most Highly Ranked Films Data\\CSV File\\top_25_recent_films_data.csv'
    dbName = 'Target Data Files\\Most Highly Ranked Films Data\\Database\\Movies.db'
    tableName = 'Target Data Files\\Most Highly Ranked Films Data\\Database\\Movies.db\\Recent_Top_25'
    
    filmsData.to_csv(csvFilepath, index=False)
    conn = sqlite3.connect(dbName)
    filmsData.to_sql(tableName, conn, if_exists='replace', index=False)

    return filmsData
