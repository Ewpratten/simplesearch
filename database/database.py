# Search database

from tinydb import TinyDB, Query
from typing import List

# DB for the entire search engine
_engine_db_path = "./engine_database.json"

# Search tools
_page = Query()

def isPageIndexed(url: str, db: TinyDB = None) -> bool:
    """Check if a url has been indexed

    Args:
        url (str): URL to check
        db (TinyDB, optional): This is only used internally. Defaults to None.

    Returns:
        bool: Has been indexed?
    """
    
    # Handle external call
    if db == None:
        with TinyDB(_engine_db_path) as db:
            return len(db.search(_page.url == url)) > 0
    else:
        return len(db.search(_page.url == url)) > 0

def indexNewWebpage(title: str, url: str, contents: List[str], timestamp: int) -> None:
    """Index a new webpage

    Args:
        title (str): Page title
        url (str): Page URL
        contents (List[str]): Page contents
        timestamp (int): Timestamp of the index
    """

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
    """Query for a page

    Args:
        keywords (List[str]): Search keywords

    Returns:
        List[dict]: All matching pages
    """ 
    
    return []