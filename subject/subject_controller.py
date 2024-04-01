from flask import Blueprint, jsonify, request
from subject.subject_model import Subject_Table, db
from flask import Blueprint
subject_bp = Blueprint('subjects', __name__)

@subject_bp.route('/subject', methods=['GET'])
def get_all_subject():
    subjects = Subject_Table.query.all()  
    subject_data = [{'subject_id': subject.subject_id, 'subject_name': subject.subject_name} for subject in subjects]
    return jsonify(subject_data)

@subject_bp.route('/subject/<int:subject_id>', methods=['GET'])
def get_subject_by_id(subject_id):
    subject = Subject_Table.query.get(subject_id)  
    if subject:
        return jsonify({'subject_id': subject.subject_id, 'subject_name': subject.subject_name})
    else:
        return jsonify({'message': 'Subject not found'}), 404

@subject_bp.route('/subject', methods=['POST'])
def add_subject():
    subject_data = request.json
    new_subject = Subject_Table(**subject_data)
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject added successfully', 'subject_id': new_subject.subject_id}), 201

@subject_bp.route('/subject/<int:subject_id>', methods=['PUT'])
def edit_subject(subject_id):
    subject = Subject_Table.query.get(subject_id)
    if not subject:
        return jsonify({'message': 'Subject not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(subject, key, value)
    db.session.commit()
    return jsonify({'message': 'Subject updated successfully'}), 200

@subject_bp.route('/subject/<int:subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    subject = Subject_Table.query.get(subject_id)
    if not subject:
        return jsonify({'message': 'Subject not found'}), 404
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'message': 'Subject deleted successfully'}), 200
