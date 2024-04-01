from extension import db

class Marks_Table(db.Model):
    __tablename__ = 'marks_table'
    mark_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.student_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject_table.subject_id'))
    exam_id = db.Column(db.Integer, db.ForeignKey('exams_table.exam_id'))
    obtained_marks = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Marks_Table(mark_id={self.mark_id}, student_id={self.student_id}, subject_id={self.subject_id}, " \
               f"exam_id={self.exam_id}, obtained_marks={self.obtained_marks})"
