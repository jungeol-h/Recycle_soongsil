from flask import Blueprint, render_template, request

from pybo import db

from pybo.models import RecycleItem


bp = Blueprint('result', __name__, url_prefix='/result')


@bp.route('/<item>')
def image_load(item):
    recycleitem= RecycleItem.query.filter_by(item_name = item).first()
    recycleitem.count +=1
    db.session.commit()
    category = recycleitem.item_category
    sub_path = []
    path = 'img/item/'+category+'/' + recycleitem.item_name + '/' + recycleitem.item_name+'.png'
    for i in range(recycleitem.size):
        sub_path.append('img/item/' + recycleitem.item_name + '/' + recycleitem.item_name+ '-'+str(i) +'.png')
    return render_template('result_page.html', item = recycleitem, subimage =sub_path, mainimage=path)
    
