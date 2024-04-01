from extension import db


class Subject_Table(db.Model):
    __tablename__ = 'subject_table'
    subject_id = db.Column(db.Integer, primary_key=True, nullable=False)
    subject_name = db.Column(db.String(50), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers_table.teacher_id'))

    def __repr__(self):
        return f"Subject_Table(subject_id={self.subject_id}, subject_name={self.subject_name}, teacher_id={self.teacher_id})"
