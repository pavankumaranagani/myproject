from extension import db

class Attendance_Table(db.Model):
    __tablename__ = 'attendance_table'
    attendance_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.student_id'))
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False) 

    def __repr__(self):
        return f"Attendance_Table(attendance_id={self.attendance_id}, student_id={self.student_id}, date={self.date}, status={self.status})"
