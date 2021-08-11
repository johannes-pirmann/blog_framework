from flask import Flask, jsonify, render_template
import markdown
from glob import glob

app = Flask(__name__, template_folder='templates')


def markdown_to_html(filename):
    open_file = open(filename, 'r')
    return markdown.markdown(open_file.read(), output='html5', encoding='utf-8')


@app.route('/')
def index():
    return markdown_to_html('blog/test.md')


@app.route('/blog')
def return_all_articles():
    filenames = glob('blog/*.md')
    articles = {}
    for file in filenames:
        link = file[:file.find('.')]
        title = link[link.find('/')+1:]
        articles[file] = {'title': title, 'link': link}
    return render_template('archive.html', articles=articles)


@app.route('/blog/<article_name>')
def render_article(article_name):
    article_name = 'blog/' + article_name + '.md'
    return markdown_to_html(article_name)


if __name__ == '__main__':
    """
    debug: Enables debug mode
    use_debugger: 
    use_reloader:
    :passthrough_errors: True to show crashes in PyCharm
    """
    app.run(debug=True, use_debugger=False, use_reloader=True, passthrough_errors=True)
