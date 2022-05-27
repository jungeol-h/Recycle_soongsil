from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect

from pybo.models import RecycleItem


bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    return render_template('main.html') 
    ##return redirect(url_for('question._list'))

@bp.route('/load/', methods=('POST',))
def load():
    item = request.form['item']
    recycleitem= RecycleItem.query.filter_by(item_name = item).first()
    print(recycleitem)
    sub_path = []
    path = 'img/item/' + recycleitem.item_name + '/' + recycleitem.item_name+'.png'
    for i in range(recycleitem.size):
        sub_path.append('img/item/' + recycleitem.item_name + '/' + recycleitem.item_name+ '-'+str(i) +'.png')
        print(path[i])
    return render_template('result_page.html', item = recycleitem, subimage =sub_path, mainimage=path)
    # else:
    #     return redirect(url_for('main.index'))

