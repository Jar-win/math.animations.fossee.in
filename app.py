from flask import Flask, render_template, Markup, abort
import json


app = Flask(__name__)
JSON_PATH = "repo-db/"

def front_page_topics(filename):
    f = open(filename, "r")
    topics = json.loads(f.read())
    return topics['topics'] 


@app.route('/')
def index():
    topics = front_page_topics(filename = "topics.json")
    return render_template('index.html', topics=topics)

@app.route('/Internship')
def internship():
    return render_template('internship.html')#"Real Analysis"

@app.route('/<page>')
def check_func(page):
    pagename = page + ".html"
    try:
        jsonname = page +  ".json"
        contents_dict = front_page_topics(filename= JSON_PATH + jsonname)
    except FileNotFoundError: 
        return "<h2> The given topic dosen't exist (yet). Please email us at animations@fossee.in if you'd want this topic to be up here (or if you want to contribute for this topic). <a href='/'>Home</a></h2>"
    return render_template(pagename, contents = contents_dict)


@app.route('/static/<page1>/<page2>/<page3>/<page4>.html')
def content(page1, page2, page3, page4):
    full_path = "static/{}/{}/{}/{}.html".format(page1, page2, page3, page4)
    try:
        with open(full_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
            abort(404)
    return render_template('content_template.html', pages = [page1, page2, page3, page4], full_text=text)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
