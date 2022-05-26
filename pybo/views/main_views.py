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
    if (item =='우산'):
        return render_template('result_page_umbrella.html')
    elif (item =='플라스틱'):
        return render_template('result_page_plastic.html')
    else:
         return redirect(url_for('main.index'))

