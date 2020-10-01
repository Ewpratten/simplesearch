# SimpleSearch
A simplistic search engine and web crawler built for learning purposes

## Crawling a new webpage from the command line

To index a new webpage from the commandline, use the `crawler` module. The following command shows it's information:

```sh
# Run help command
bazel run //crawler -- -h

# Usage
usage: crawler [-h] [-d DEPTH] [-w WIDTH] url

Web crawler CLI for SimpleSearch

positional arguments:
  url                   Base URL to start crawling at

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        Maximum recursive depth
  -w WIDTH, --width WIDTH
                        Maximum number of search branches per page
```

For example, I like to use the following command to test the crawler:

```sh
bazel run //crawler -- https://retrylife.ca -d 2 -w 5
```

