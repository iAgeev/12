from json import JSONDecodeError

from flask import Blueprint, render_template, request, logging

from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Searching...')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.info('File not found')
        return 'File not found, try new file'
    except JSONDecodeError:
        return 'File is not valid'
    return render_template('post_list.html', query=search_query, posts=posts)
