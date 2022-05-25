from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    return render_template('main.html') 
    ##return redirect(url_for('question._list'))

@bp.route('/load/', methods=('POST',))
def load():
    item = request.form['item']
    return redirect(url_for('result.detail'))

