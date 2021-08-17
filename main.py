from flask import Flask, abort, request
import markdown
import frontmatter
from jinja2 import TemplateNotFound
from articles.articles import article_page
from handlers import analytics

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


@app.route('/')
def index():
    try:
        print(request.path)
        analytics.increase_view_count(request.path)
        return 'Index'
    except (FileNotFoundError, TemplateNotFound):
        abort(404)


@app.route('/page/<page_name>')
def show_page(page_name):
    try:
        page = frontmatter.load('page/' + page_name + '.md')
        analytics.increase_view_count(request.path)
        return markdown.markdown(page.content)
    except (FileNotFoundError, TemplateNotFound):
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    analytics.increase_view_count(request.path)
    return '404', 404


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=True, passthrough_errors=True)
