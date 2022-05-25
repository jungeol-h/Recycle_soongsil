from flask import Blueprint, render_template

from pybo.models import RecycleItem


bp = Blueprint('result', __name__, url_prefix='/result')


@bp.route('/detail/<')
def detail():
    item = RecycleItem.query.get_or_404()
    return render_template('result_page.html', item=item) 
    ##return redirect(url_for('question._list'))