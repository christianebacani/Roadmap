# Load to CSV Filepath
def load_to_csv(df, csvFilepath):
    df.to_csv(csvFilepath, index=False)




# Load to JSON Filepath
def load_to_json(df, jsonFilepath):
    with open(jsonFilepath, 'w') as f:
        f.write(df.to_json(orient='records'))
    f.close()




# Load to XML Filepath
def load_to_xml(df, xmlFilepath):
    df.to_xml(path_or_buffer=xmlFilepath, root_name='Earthquake_Data', row_name='Earthquake', index=False, parser='lxml')




# Load to Local SQLite Database
def load_to_sqlite_db(df, conn, tableName):
    df.to_sql(tableName, conn, if_exists='replace', index=False)



