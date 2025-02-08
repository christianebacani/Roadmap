# 1148. Article Views I
# Category : Pandas

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authorsViewOwnArticle = []
    
    for _, row in views.iterrows():
        authorId = row.get('author_id')
        viewerId = row.get('viewer_id')
        
        if (authorId == viewerId) and (authorId not in authorsViewOwnArticle):
            authorsViewOwnArticle.append(authorId)
    
    sortedAuthorsViewOwnArticle = sorted(authorsViewOwnArticle)
    
    return pd.DataFrame({'id' : sortedAuthorsViewOwnArticle})
    