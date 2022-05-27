from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class RecycleItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text(), nullable=False)
    item_sentence = db.Column(db.Text(), nullable=False)
    item_image = db.Column(db.String(100), default='img/item/우산/0.png')
    size = db.Column(db.Integer, nullable=True, server_default='1')
    item_subimage =  db.Column(db.String(100), default='img/item/우산/0.png')
