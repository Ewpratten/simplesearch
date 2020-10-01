# Task class for recursive web crawling

import requests
import time

from typing import Generator
from bs4 import BeautifulSoup

from database.database import indexNewWebpage

class WebCrawlTask(object):
    """Task class for recursive web crawling"""

    url: str
    max_depth: int
    max_width: int

    def __init__(self, url: str, max_depth: int, max_width: int):
        """Create a WebCrawlTask

        Args:
            url (str): Url to crawl
            max_depth (int): Maximum depth
            max_width (int): Maximum width
        """
        self.url = url
        self.max_depth = max_depth
        self.max_width = max_width

    def run(self) -> Generator:
        
        # Make a request to the given page
        try:
            response = requests.get(self.url)
        except requests.exceptions.ConnectionError as e:
            return

        # Stop if this page does not exist
        if int(response.status_code / 100) != 2:
            return

        # Get the raw HTML
        raw_page_html: str = response.text

        # Build a page parser
        parser: BeautifulSoup = BeautifulSoup(raw_page_html, "html.parser")

        # Make an index call
        self._indexPage(parser)

        # Search for every sublink
        for a_tag in parser.find_all("a"):

            # Ensure there is HREF data
            if not "href" in a_tag.attrs:
                continue

            # Sanitize the inputs
            new_url = a_tag.attrs["href"]

            source_url_parts = self.url.split("/")
            source_url_protocol = source_url_parts[0]
            source_url_domain = source_url_parts[2]

            # Handle a leading single slash
            if len(new_url) >= 2 and new_url[0] == "/" and new_url[1] != "/":
                new_url = f"{source_url_protocol}//{source_url_domain}{new_url}"
            if new_url == "/":
                new_url = f"{source_url_protocol}//{source_url_domain}"

            # Handle a leading double slash
            if len(new_url) >= 2 and new_url[0] == "/" and new_url[1] == "/":
                new_url = f"https:{new_url}"

            # Build a new subtask if this is not the last in its chain
            if self.max_depth > 1:
                yield WebCrawlTask(new_url, self.max_depth - 1, self.max_width)

        return

    def getURL(self) -> str:
        return self.url

    def _indexPage(self, contents: BeautifulSoup) -> None:
        
        # Get page data
        page_title = contents.find("title").contents
        page_url = self.url

        all_p_tags = contents.find_all("p")
        if len(all_p_tags) > 0:
            page_info = all_p_tags[0].contents[0].split(" ")
        else:
            page_info = []

        # Make a DB write call
        indexNewWebpage(page_title, page_url, page_info, int(time.time()))
