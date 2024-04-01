# app/controllers/students_controller.py

from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from student.student_model import Student_Table, db

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['GET'])
def get_all_students():
    students = Student_Table.query.all()
    student_data = [{'student_id': student.student_id, 'name': student.first_name + " "+student.last_name} for student in students]
    return jsonify(student_data)

@students_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = Student_Table.query.filter_by(student_id=student_id).first()
    if student:
        return jsonify({'student_id': student.student_id, 'name': student.first_name + " "+student.last_name })
    else:
        return jsonify({'message': 'Student not found'}), 404

@students_bp.route('/students', methods=['POST'])
def add_student():
    student_data = request.json
    new_student = Student_Table(**student_data)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully', 'student_id': new_student.student_id}), 201

@students_bp.route('/students/<int:student_id>', methods=['PUT'])
def edit_student(student_id):
    student = Student_Table.query.filter_by(student_id=student_id).first()
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(student, key, value)
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'}), 200

@students_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student_Table.query.filter_by(student_id=student_id).first()
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200
