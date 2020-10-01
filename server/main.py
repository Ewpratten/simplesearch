# Web backend

import flask

from database.database import query


app = flask.Flask(__name__)

# Simplistic list of html sanatization rules
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

@app.route("/submit")
def handleCrawlRequest():
    return "Crawl"

@app.route("/search/<keywords>")
def handleSearchFirstPage(keywords: str) -> flask.Response:
    return handleSearch(keywords, 1)

@app.route("/search/<keywords>/<int:page>")
def handleSearch(keywords: str, page: int) -> flask.Response:

    # Split the keyword string into something useful
    keyword_tokens = cleanString(keywords).split("%20")

    # Perform a database search
    results = query(keyword_tokens)

    print(results)

    return "Search page " + str(page)

if __name__ == "__main__":
    app.run(debug=True)