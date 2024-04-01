from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from fee.fee_model import Fees_Table, db
from flask import Blueprint

fees_bp = Blueprint('fees', __name__)

@fees_bp.route('/fees', methods=['GET'])
def get_all_fees():
    fees = Fees_Table.query.all()
    fee_data = [{'fee_id': fee.fee_id, 'name': fee.amount} for fee in fees]
    return jsonify(fee_data)

@fees_bp.route('/fees/<int:fee_id>', methods=['GET'])
def get_fee_by_id(fee_id):
    fee = Fees_Table.query.filter_by(fee_id=fee_id).first()
    if fee:
        return jsonify({'fee_id': fee.fee_id, 'name': fee.amount})
    else:
        return jsonify({'message': 'Fee not found'}), 404

@fees_bp.route('/fees', methods=['POST'])
def add_fee():
    fee_data = request.json
    new_fee = Fees_Table(**fee_data)
    db.session.add(new_fee)
    db.session.commit()
    return jsonify({'message': 'Fee added successfully', 'fee_id': new_fee.fee_id}), 201

@fees_bp.route('/fees/<int:fee_id>', methods=['PUT'])
def edit_fee(fee_id):
    fee = Fees_Table.query.filter_by(fee_id=fee_id).first()
    if not fee:
        return jsonify({'message': 'Fee not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(fee, key, value)
    db.session.commit()
    return jsonify({'message': 'Fee updated successfully'}), 200

@fees_bp.route('/fees/<int:fee_id>', methods=['DELETE'])
def delete_fee(fee_id):
    fee = Fees_Table.query.filter_by(fee_id=fee_id).first()
    if not fee:
        return jsonify({'message': 'Fee not found'}), 404
    db.session.delete(fee)
    db.session.commit()
    return jsonify({'message': 'Fee deleted successfully'}), 200
