from flask import jsonify
from app.util.validators import string_to_date
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager
from app.models.transaction import TransactionModel
from app.util.logz import create_logger
from sqlalchemy import func
from app.config.db import db


class TransactionList(Resource):
    def __init__(self):
        self.logger = create_logger()

    @jwt_required()
    
    def post(self):
        
        current_user = get_jwt_identity()
        
        lastJson = []
        len_currency = []
        
        parser = reqparse.RequestParser()
        parser.add_argument('fromDate', type=str, required=True,
                            help='Not Blank')
        parser.add_argument('toDate', type=str, required=True,
                            help='Not Blank')
        parser.add_argument('merchant', type=int, required=False)
        parser.add_argument('acquirer', type=int, required=False)

        data = parser.parse_args()
        fromDate = data['fromDate']
        toDate = data['toDate']
        merchant = data['merchant']
        acquirer = data['acquirer']

        date_time_obj_fromdate = string_to_date(fromDate)
        date_time_obj_todate = string_to_date(toDate)

        user = db.session.query(TransactionModel).filter(db.func.date(TransactionModel.transactiondate) >= date_time_obj_fromdate,
                                                db.func.date(TransactionModel.transactiondate) <= date_time_obj_todate,
                                                TransactionModel.merchant == merchant,
                                                TransactionModel.acquirer == acquirer).all()
        
        for x in range(len(user)):
            len_currency.append(user[x].currency)
        for x in set(len_currency):
            
            count = db.session.query(TransactionModel).filter(db.func.date(TransactionModel.transactiondate) >= date_time_obj_fromdate,
                                        db.func.date(TransactionModel.transactiondate) <= date_time_obj_todate,
                                        TransactionModel.merchant == merchant,
                                        TransactionModel.acquirer == acquirer,
                                        TransactionModel.currency == x).count()
        
            sum = db.session.query(TransactionModel).filter(db.func.date(TransactionModel.transactiondate) >= date_time_obj_fromdate,
                                        db.func.date(TransactionModel.transactiondate) <= date_time_obj_todate,
                                        TransactionModel.merchant == merchant,
                                        TransactionModel.acquirer == acquirer,
                                        TransactionModel.currency == x).with_entities(func.sum(TransactionModel.amount)).scalar()
            
            lastJson.append({
                "count":count,
                "total":sum,
                "currency":x
            })
                
        
        return jsonify(
                status="APPROVED",
                response=lastJson
                )
