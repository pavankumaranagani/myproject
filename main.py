from flask import Flask
from extension import db
from student.student_controller import students_bp
from classes.classes_controller import classes_bp
from teacher.teacher_controller import teacher_bp
from exam.exam_controller import exam_bp
from fee.fee_controller import fees_bp
from marks.marks_controller import marks_bp
from subject.subject_controller import subject_bp
from attendance.attendance_controller import attendance_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pavan@localhost/pavan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register blueprints with the common URL prefix
app.register_blueprint(students_bp, url_prefix='/api')
app.register_blueprint(classes_bp, url_prefix='/api')
app.register_blueprint(teacher_bp, url_prefix='/api')
app.register_blueprint(exam_bp, url_prefix='/api')
app.register_blueprint(fees_bp, url_prefix='/api')
app.register_blueprint(marks_bp, url_prefix='/api')
app.register_blueprint(subject_bp, url_prefix='/api')
app.register_blueprint(attendance_bp, url_prefix='/api')

with app.app_context():
        db.init_app(app)
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
