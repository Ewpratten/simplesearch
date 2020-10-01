# Web backend

import flask

from database.database import query
from crawler.lib import taskmanager

from threading import Thread
from typing import List


app = flask.Flask(__name__)

# Simplistic list of html sanitization rules
html_cleanup = {
    "/": "",
    " ": "%20",
    "?": "",
    "&": ""
}

def cleanString(dirty: str) -> str:
    for entry in html_cleanup:
        dirty = dirty.replace(entry, html_cleanup[entry])
    return dirty

_isHandlingSubmissionRightNow = False

def handleSubmissionRequest(url: str):
    _isHandlingSubmissionRightNow = True
    taskmanager.begin(url, 15, 10)
    _isHandlingSubmissionRightNow = False


@app.route("/", methods=["GET", "POST"])
def handleSearchIndex():
    # Handle post
    if flask.request.method == 'POST':
        # Get the search terms
        if flask.request.values.get('q'):

            # Clean up the search
            search = cleanString(flask.request.values.get('q'))

            # Redirect to search page
            response = flask.make_response("Redirecting", 302)
            response.headers["Location"] = f"/search/{search}"
            return response
    
    # Return search page
    return flask.make_response(flask.render_template("index.html"))

@app.route("/about")
def handleAbout():
    return flask.make_response(flask.render_template("about.html"))

active_threads:List[Thread] = []

@app.route("/submit", methods=["GET", "POST"])
def handleCrawlRequest():
    # Handle post
    if flask.request.method == 'POST':
        # Get the requested URL
        if flask.request.values.get('u'):
            # Remove any inactive threads
            for thread in active_threads:
                if not thread.is_alive:
                    del thread

            # Check if a task is being run right now
            if len(active_threads) > 0:

                # Redirect to waiting page
                flask.make_response(flask.render_template("suggest-fail.html"))
            else:

                # Spin up a crawler instance
                t = Thread(target=handleSubmissionRequest, args=[flask.request.values.get('u')])
                t.start()
                active_threads.append(t)

        # Redirect home
        response = flask.make_response("Redirecting", 302)
        response.headers["Location"] = f"/"
        return response

    return flask.make_response(flask.render_template("suggest.html"))

@app.route("/search/<keywords>")
def handleSearchFirstPage(keywords: str) -> flask.Response:
    response = flask.make_response("Redirecting", 302)
    response.headers["Location"] = f"/search/{keywords}/1"
    return response

@app.route("/search/<keywords>/<int:page>", methods=["GET", "POST"])
def handleSearch(keywords: str, page: int) -> flask.Response:

    # Handle post
    if flask.request.method == 'POST':
        # Get the search terms
        if flask.request.values.get('q'):

            # Clean up the search
            search = cleanString(flask.request.values.get('q'))

            # Redirect to search page
            response = flask.make_response("Redirecting", 302)
            response.headers["Location"] = f"/search/{search}"
            return response

    # Split the keyword string into something useful
    keyword_tokens = cleanString(keywords).split("%20")

    # Perform a database search
    results = query(keyword_tokens)
    num_results = len(results)
    results_per_page = 5
    num_pages = int(num_results / results_per_page)

    # Get the results for this page
    page_results = results[(results_per_page * (page - 1)) :][: results_per_page ]

    return flask.make_response(flask.render_template("results.html", page_num=page, keywords=keyword_tokens, results=page_results, num_pages = num_pages))

if __name__ == "__main__":
    app.run(debug=True)