
from flask import Flask, jsonify, render_template, abort
import markdown
from glob import glob
import frontmatter
from datetime import date

from jinja2 import TemplateNotFound

from articles.articles import article_page

app = Flask(__name__, template_folder='templates')
app.register_blueprint(article_page)


def markdown_to_html(filename: str):
    """
    Converts a markdown file to html.
    :param filename:
        a markdown file
    :return:
        content of the markdown file as html
    """
    open_file = open(filename, 'r')
    return markdown.markdown(open_file.read())


@staticmethod
def increase_view_count(route: str) -> None:
    """
    Takes current route and add one view to database.
    :param route:
        Takes the current route
    :return:
    """
    pass


@app.route('/')
def index():
    try:
        return 'Index'
    except (FileNotFoundError, TemplateNotFound):
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return '404', 404


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=True, passthrough_errors=True)
