# Search database

from tinydb import TinyDB, Query
from typing import List
import os

# DB for the entire search engine
_engine_db_path = os.path.expanduser("~/simplesearch_engine_database.json")
print(f"Using database at: {os.path.abspath(_engine_db_path)}")


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
            table = db.table("search", cache_size=0)
            return len(table.search(_page.url == url)) > 0
    else:
        table = db.table("search", cache_size=0)
        return len(table.search(_page.url == url)) > 0

def indexNewWebpage(title: str, url: str, contents: List[str], timestamp: int) -> None:
    """Index a new webpage

    Args:
        title (str): Page title
        url (str): Page URL
        contents (List[str]): Page contents
        timestamp (int): Timestamp of the index
    """

    # Force all the contents to be lowercase
    lower_contents = []
    for content in contents:
        lower_contents.append(content.lower())

    with TinyDB(_engine_db_path) as db:
        table = db.table("search", cache_size=0)
        # If an index exists for this page, update it
        if isPageIndexed(url, db=db):
            table.update({
                "title": title,
                "url": url,
                "contents": lower_contents,
                "timestamp":timestamp
            },_page.url == url)
        else:
            table.insert({
                "title": title,
                "url": url,
                "contents": lower_contents,
                "timestamp":timestamp
            })

def query(keywords: List[str]) -> List[dict]:
    """Query for a page

    Args:
        keywords (List[str]): Search keywords

    Returns:
        List[dict]: All matching pages
    """ 

    # Determine the number of keywords
    num_keywords = len(keywords)

    # Convert the keywords to lowercase
    lower_keywords = []
    for keyword in keywords:
        lower_keywords.append(keyword.lower())

    def comparator(contents):
        found_keys = 0

        # Searches for keywords and keyword parts in the resulting texts
        for word in contents:
            for keyword in lower_keywords:
                if word.lower() == keyword:
                    found_keys += 1
                if word.lower() and keyword in word.lower():
                    found_keys += 1
                    
        return  (found_keys >= (num_keywords / 2))
        # return any(lower_keywords == contents[i:num_keywords+i] for i in range(len(contents) - num_keywords+1))

    with TinyDB(_engine_db_path, cache_size=0) as db:
        db.clear_cache()
        table = db.table("search", cache_size=0)
        # Checks for permutations of the keywords in each page's contents
        return table.search(_page.contents.test(comparator))