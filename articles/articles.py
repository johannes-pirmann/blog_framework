from datetime import date
from glob import glob
import frontmatter
import markdown
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

article_page = Blueprint('article_page', __name__, template_folder='templates')


def fetch_all_articles():
    return glob('blog/*.md')


@article_page.route('/blog')
def return_all_posted_articles():
    try:
        filenames = fetch_all_articles()
        current_date = date.today().strftime('%Y-%m-%d')
        articles = {}
        for file in filenames:
            file_options = {
                'link': '',
                'title': '',
                'date': '',
                'description': '',
                'draft': 'False',
                'expiry_date': '',
                'keywords': '',
                'lastmod': '',
                'summary': '',
                'slug': ''
            }
            article = frontmatter.load(file)
            for key in article.keys():
                file_options[key] = article[key]
            print(file_options)
            if file_options['date'] <= current_date and file_options['draft'] is not True:
                articles[file] = file_options
            else:
                pass
        return render_template('archive.html', articles=articles)
    except (FileNotFoundError, TemplateNotFound):
        abort(404)


@article_page.route('/blog/<article_name>')
def show_article(article_name):
    try:
        post = frontmatter.load('blog/' + article_name + '.md')
        return markdown.markdown(post.content)
    except (FileNotFoundError, TemplateNotFound):
        abort(404)


@article_page.route('/author/<author_name>')
def show_author(author_name):
    pass
