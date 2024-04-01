from extension import db


class Exams_Table(db.Model):  
    __tablename__ = 'exams_table'
    exam_id = db.Column(db.Integer, primary_key=True, nullable=False)
    exam_name = db.Column(db.String(50), nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Exams_Table(exam_id={self.exam_id}, exam_name={self.exam_name}, exam_date={self.exam_date}, total_marks={self.total_marks})"

