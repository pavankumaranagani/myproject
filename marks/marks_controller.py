from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marks.marks_models import Marks_Table, db  
from flask import Blueprint

marks_bp = Blueprint('marks', __name__)

@marks_bp.route('/marks', methods=['GET'])
def get_all_marks():
    marks = Marks_Table.query.all()
    marks_data = [{'marks_id': mark.marks_id, 'name': mark.obtained_marks} for mark in marks]
    return jsonify(marks_data)

@marks_bp.route('/marks/<int:mark_id>', methods=['GET'])
def get_marks_by_id(mark_id):
    mark = Marks_Table.query.filter_by(mark_id=mark_id).first()
    if mark:
        return jsonify({'mark_id': mark.mark_id, 'obtained_marks': mark.obtained_marks})
    else:
        return jsonify({'message': 'Marks not found'}), 404

@marks_bp.route('/marks', methods=['POST'])
def add_marks():
    mark_data = request.json
    new_mark = Marks_Table(**mark_data)
    db.session.add(new_mark)
    db.session.commit()
    return jsonify({'message': 'Marks added successfully', 'marks_id': new_mark.marks_id}), 201

@marks_bp.route('/marks/<int:mark_id>', methods=['PUT'])
def edit_marks(mark_id):
    mark = Marks_Table.query.filter_by(mark_id=mark_id).first()
    if not mark:
        return jsonify({'message': 'Marks not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(mark, key, value)
    db.session.commit()
    return jsonify({'message': 'Marks updated successfully'}), 200

@marks_bp.route('/marks/<int:mark_id>', methods=['DELETE'])
def delete_marks(mark_id):
    mark = Marks_Table.query.filter_by(mark_id=mark_id).first()
    if not mark:
        return jsonify({'message': 'Marks not found'}), 404
    db.session.delete(mark)
    db.session.commit()
    return jsonify({'message': 'Marks deleted successfully'}), 200
