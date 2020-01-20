#import flask
#rename the python file app.py (convention)
from flask import Flask, render_template, redirect, url_for, request

app = Flask("webapp")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# define home
@app.route("/")
def home():
    return get_html("index")

#I think the /firstname route is not needed. It seems to be easier to solve this with javascript (see index.html)

#setup database
def get_db():
    webappdb = open("webappdb.txt")
    content = webappdb.read()
    webappdb.close()
    results = content.split("\n")
    results.pop(len(results) -1)
    return results

#adding items to the database (create a note)
@app.route('/note')
def add_note():
    add_note_todb = request.args.get("note")
    file = open('webappdb.txt', 'a')
    file.write(str(add_note_todb) + "\n")
    return redirect(url_for('result'))

#show results on separate page
@app.route('/results')
def result():
    html_page = get_html("results")
    results = get_db()
    actual_values = ""
    for result in results:
        actual_values += "<p>" + result + "</p>"
    return html_page.replace("$$RESULT$$", actual_values)

#search for notes on homepaage
@app.route("/search")
def search():
    html_page = get_html("results")
    query = request.args.get("query")
    results = get_db()
    searchresult = ""
    for result in results:
        if result.lower().find(query.lower()) != -1:
            searchresult += "<p>" + result + "</p>"
    if searchresult == "":
        searchresult = "<p>No luck! We couldn't find a note. Sorry!</p>"
    return html_page.replace("$$RESULT$$", searchresult )
