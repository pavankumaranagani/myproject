from flask import Blueprint, jsonify, request
from teacher.teacher_model import Teachers_Table, db
from flask import Blueprint

teacher_bp = Blueprint('teachers', __name__)  

@teacher_bp.route('/teacher', methods=['GET'])  
def get_all_teacher():  
    teachers = Teachers_Table.query.all()
    teacher_data = [{'teacher_id': teacher.teacher_id , 'teacher_name': teacher.first_name + " "+teacher.last_name} for teacher in teachers]  
    return jsonify(teacher_data)

@teacher_bp.route('/teacher/<int:teacher_id>', methods=['GET'])  
def get_teacher_by_id(teacher_id):  
    teacher = Teachers_Table.query.get(teacher_id)  
    if teacher:
        return jsonify({'teacher_id': teacher.teacher_id, 'teacher_name': teacher.first_name + " "+teacher.last_name})  
    else:
        return jsonify({'message': 'Teacher not found'}), 404

@teacher_bp.route('/teacher', methods=['POST'])  
def add_teacher(): 
    teacher_data = request.json
    new_teacher = Teachers_Table(**teacher_data)  
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher added successfully', 'teacher_id': new_teacher.teacher_id}), 201  

@teacher_bp.route('/teacher/<int:teacher_id>', methods=['PUT'])  
def edit_teacher(teacher_id):  
    teacher = Teachers_Table.query.get(teacher_id)
    if not teacher:
        return jsonify({'message': 'Teacher not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(teacher, key, value)
    db.session.commit()
    return jsonify({'message': 'Teacher updated successfully'}), 200

@teacher_bp.route('/teacher/<int:teacher_id>', methods=['DELETE'])  
def delete_teacher(teacher_id):  
    teacher = Teachers_Table.query.get(teacher_id)  
    if not teacher:
        return jsonify({'message': 'Teacher not found'}), 404
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher deleted successfully'}), 200
