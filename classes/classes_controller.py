# app/controllers/classes_controller.py

from flask import Blueprint, jsonify, request
from classes.classes_model import Classes_Table, db
from flask import Blueprint


classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/classes', methods=['GET'])
def get_all_classes():
    classes = Classes_Table.query.all()
    class_data = [{'class_id': cls.class_id, 'class_name': cls.class_name} for cls in classes]
    return jsonify(class_data)

@classes_bp.route('/classes/<int:class_id>', methods=['GET'])
def get_class_by_id(class_id):
    cls = Classes_Table.query.get(class_id)
    if cls:
        return jsonify({'class_id': cls.class_id, 'class_name': cls.class_name})
    else:
        return jsonify({'message': 'Class not found'}), 404

@classes_bp.route('/classes', methods=['POST'])
def add_class():
    class_data = request.json
    new_class = Classes_Table(**class_data)
    db.session.add(new_class)
    db.session.commit()
    return jsonify({'message': 'Class added successfully', 'class_id': new_class.class_id}), 201

@classes_bp.route('/classes/<int:class_id>', methods=['PUT'])
def edit_class(class_id):
    cls = Classes_Table.query.get(class_id)
    if not cls:
        return jsonify({'message': 'Class not found'}), 404
    new_data = request.json
    for key, value in new_data.items():
        setattr(cls, key, value)
    db.session.commit()
    return jsonify({'message': 'Class updated successfully'}), 200

@classes_bp.route('/classes/<int:class_id>', methods=['DELETE'])
def delete_class(class_id):
    cls = Classes_Table.query.get(class_id)
    if not cls:
        return jsonify({'message': 'Class not found'}), 404
    db.session.delete(cls)
    db.session.commit()
    return jsonify({'message': 'Class deleted successfully'}), 200
