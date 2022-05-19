from flask import Blueprint, render_template

from pybo.models import Question
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('Question_list.html', question_list=question_list)