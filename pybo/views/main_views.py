from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect

from pybo.models import RecycleItem


bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    item = RecycleItem.query.order_by(RecycleItem.count.desc())
    print(item)

    return render_template('main.html',freqitem = item)


@bp.route('/load/', methods=('POST',))
def load():
    item = request.form['item']
    return redirect(url_for('result.image_load', item=item))
    # else:
    #   

"""
old version
def load():
    item = request.form['item']
    recycleitem= RecycleItem.query.filter_by(item_name = item).first()
    print(recycleitem)
    category = recycleitem.item_category
    sub_path = []
    path = 'img/item/'+category+'/' + recycleitem.item_name + '/' + recycleitem.item_name+'.png'
    for i in range(recycleitem.size):
        sub_path.append('img/item/' + recycleitem.item_name + '/' + recycleitem.item_name+ '-'+str(i) +'.png')
        print(path[i])
    return render_template('result_page.html', item = recycleitem, subimage =sub_path, mainimage=path)
"""