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
    si_rec= RecycleItem.query.filter_by(item_category = category)
    sub_path = []
    path = 'img/item/'+category+'/' + recycleitem.item_name + '/' + recycleitem.item_name+'.png'
    si_rec_count = si_rec.count()
    for i in range(recycleitem.size):
        try:
            sub_path.append('img/item/' + category +'/'+recycleitem.item_name + '/' + recycleitem.item_name+str(i+1)+'.png')
        except: 
            sub_path.append('img/item/' + '숫자' +'/'+str(i+1)+'.png')
            print('sub_path[i]')

    ## 한줄요약 불러오기
    try:
        f = open('pybo/static/img/item/'+ category +'/'+recycleitem.item_name + '/' + recycleitem.item_name + '.txt', 'r', encoding='UTF8')
        one_sentence = f.readline()
    except: one_sentence = '한줄 요약이 없습니다.'


    ## 처리절차 불러오기
    try:
        sequence = []
        for i in range(recycleitem.size):
            sequence.append(f.readline())
    except: sequence.append('내용이 없습니다.')





    return render_template('result_page.html', item = recycleitem, subimage =sub_path, mainimage=path, si_rec = si_rec, si_rec_count = si_rec_count, one_sentence = one_sentence, sequence=sequence)
    
