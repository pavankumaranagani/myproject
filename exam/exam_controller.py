from flask import Blueprint, jsonify, request
from exam.exam_model import Exams_Table, db

exam_bp = Blueprint('exams', __name__)  

@exam_bp.route('/exam', methods=['GET']) 
def get_all_exam():  
    exams = Exams_Table.query.all()  
    exam_data = [{'exam_id': exam.exam_id, 'exam_name': exam.exam_name} for exam in exams]  
    return jsonify(exam_data)

@exam_bp.route('/exam/<int:exam_id>', methods=['GET'])  
def get_exam_by_id(exam_id):  
    exam = Exams_Table.query.get(exam_id)  
    if exam:
        return jsonify({'exam_id': exam.exam_id, 'exam_name': exam.exam_name})  
    else:
        return jsonify({'message': 'Exam not found'}), 404

@exam_bp.route('/exam', methods=['POST'])  
def add_exam():  
    exam_data = request.json  
    new_exam = Exams_Table(**exam_data)  
    db.session.add(new_exam)
    db.session.commit()
    return jsonify({'message': 'Exam added successfully', 'exam_id': new_exam.exam_id}), 201

@exam_bp.route('/exam/<int:exam_id>', methods=['PUT'])  
def edit_exam(exam_id):  
    exam = Exams_Table.query.get(exam_id)  
    if not exam:
        return jsonify({'message': 'Exam not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(exam, key, value)
    db.session.commit()
    return jsonify({'message': 'Exam updated successfully'}), 200

@exam_bp.route('/exam/<int:exam_id>', methods=['DELETE'])  
def delete_exam(exam_id):  
    exam = Exams_Table.query.get(exam_id)  
    if not exam:
        return jsonify({'message': 'Exam not found'}), 404
    db.session.delete(exam)
    db.session.commit()
    return jsonify({'message': 'Exam deleted successfully'}), 200
