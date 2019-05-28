from flask import render_template
from . import main
from .forms import CommentForm

# Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    return render_template('index.html')

# @main.route('/comments/<int:id>', methods = ['GET','POST'])
# @login_required
# def pitch
