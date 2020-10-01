# Search database

from tinydb import TinyDB, Query
from typing import List

# DB for the entire search engine
_engine_db_path = "./engine_database.json"

# Search tools
_page = Query()

def isPageIndexed(url: str, db: TinyDB = None):
    # Handle external call
    if db == None:
        with TinyDB(_engine_db_path) as db:
            return len(db.search(_page.url == url)) > 0
    else:
        return len(db.search(_page.url == url)) > 0

def indexNewWebpage(title: str, url: str, contents: List[str], timestamp: int) -> None:
    with TinyDB(_engine_db_path) as db:
        # If an index exists for this page, update it
        if isPageIndexed(url, db=db):
            db.update({
                "title": title,
                "url": url,
                "contents": contents,
                "timestamp":timestamp
            },_page.url == url)
        else:
            db.insert({
                "title": title,
                "url": url,
                "contents": contents,
                "timestamp":timestamp
            })

def query(keywords: List[str]) -> List[dict]:
    return []