from app.config.db import db


class TransactionModel(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.Integer)
    acquirer = db.Column(db.Integer)
    currency = db.Column(db.String())
    amount = db.Column(db.Integer)
    transactiondate = db.Column(db.DateTime(timezone=False))

    def __init__(self, alert):
        self.alert = alert

    def json(self):
        return {'data': self.alert}

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()  

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

