from flask import Blueprint, jsonify, request
from attendance.attendance_model import Attendance_Table, db
from flask import Blueprint

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance', methods=['GET'])
def get_all_attendance():
    attendance = Attendance_Table.query.all()
    attendance_data = [{'attendance_id': attd.attendance_id, 'attendance_status': attd.status} for attd in attendance]
    return jsonify(attendance_data)

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['GET'])
def get_attendance_by_id(attendance_id):
    attd = Attendance_Table.query.get(attendance_id)
    if attd:
        return jsonify({'attendance_id': attd.attendance_id, 'attendance_status': attd.status})
    else:
        return jsonify({'message': 'Attendance not found'}), 404

@attendance_bp.route('/attendance', methods=['POST'])
def add_attendance():
    attendance_data = request.json
    new_attendance = Attendance_Table(**attendance_data)
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance added successfully', 'attendance_id': new_attendance.attendance_id}), 201

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['PUT'])
def edit_attendance(attendance_id):
    attd = Attendance_Table.query.get(attendance_id)
    if not attd:
        return jsonify({'message': 'Attendance not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(attd, key, value)
    db.session.commit()
    return jsonify({'message': 'Attendance updated successfully'}), 200

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['DELETE'])
def delete_attendance(attendance_id):
    attd = Attendance_Table.query.get(attendance_id)
    if not attd:
        return jsonify({'message': 'Attendance not found'}), 404
    db.session.delete(attd)
    db.session.commit()
    return jsonify({'message': 'Attendance deleted successfully'}), 200
