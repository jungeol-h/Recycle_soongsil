from operator import itemgetter
from flask import Blueprint, url_for, render_template, request, flash
from werkzeug.utils import redirect

from pybo.models import RecycleItem, Question


bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    item = RecycleItem.query.order_by(RecycleItem.count.desc())
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('main.html',freqitem = item, freqquestion = question_list)

@bp.route('/load/', methods=["POST"])
def load():
    itemname = request.form['item']
    validitem = RecycleItem.query.filter_by(item_name =itemname).first()
    item = RecycleItem.query.order_by(RecycleItem.count.desc())
    question_list = Question.query.order_by(Question.create_date.desc())
    if not validitem:
        flash("아직 등록되지 않은 쓰레기입니다ㅠㅠ")
        return render_template('main.html',freqitem = item, freqquestion = question_list)
    else :
        return redirect(url_for('result.image_load', item=itemname))


@bp.route('/load/<itemname>', methods=["GET"])
def load2(itemname):
    name=itemname
    return redirect(url_for('result.image_load', item=name))


@bp.route('/request_img/<item>')
def request_img(item):
    recycleitem= RecycleItem.query.filter_by(item_name = item).first()
    path = 'img/item/'+category+'/' + recycleitem.item_name + '/' + recycleitem.item_name+'.png'
    return path

@bp.route('/request_text/<item>')
def request_text(item):
    recycleitem= RecycleItem.query.filter_by(item_name = item).first()
    return recycleitem.itemname


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