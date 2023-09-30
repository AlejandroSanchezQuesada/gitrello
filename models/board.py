from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Board(db.Model):
    __tablename__ = 'board'

    # Columns
    id_list = db.Column(db.String(255), nullable=False)
    name_list = db.Column(db.String(255), nullable=False)
    id_card = db.Column(db.String(255), unique=True, nullable=False)
    desc_card = db.Column(db.Text, nullable=True)

    # Constructor
    def __init__(self, id_list=None, name_list=None, id_card=None, desc_card=None):
        self.id_list = id_list
        self.name_list = name_list
        self.id_card = id_card
        self.desc_card = desc_card
