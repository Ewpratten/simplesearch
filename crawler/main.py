# Webcrawler CLI

import argparse
from crawler.lib import taskmanager

def main() -> None:

    # Handle CLI arguments
    ap = argparse.ArgumentParser(prog="crawler", description="Web crawler CLI for SimpleSearch")
    ap.add_argument("url", help="Base URL to start crawling at")
    ap.add_argument("-d","--depth", help="Maximum recursive depth", default=5, type=int)
    ap.add_argument("-w", "--width", help="Maximum number of search branches per page", default=100, type=int)
    args = ap.parse_args()

    print(f"Beginning crawl task for URL: {args.url}")
    taskmanager.begin(args.url, args.depth, args.width)


if __name__ == "__main__":
    main()