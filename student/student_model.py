from extension import db


class Student_Table(db.Model):
    __tablename__ = 'student_table'
    student_id = db.Column(db.Integer, primary_key=True, nullable=False)  
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)  
    date_of_birth = db.Column(db.Date, nullable=False)  
    gender = db.Column(db.String(10), nullable=False)  
    address = db.Column(db.String(255), nullable=False)  
    guardian_name = db.Column(db.String(100), nullable=False) 
    contact_number = db.Column(db.String(10), nullable=False)   
    class_id = db.Column(db.Integer, db.ForeignKey('classes_table.class_id'), nullable=False)
    admission_date = db.Column(db.Date, nullable=False)
    classes = db.relationship('Classes_Table', backref='students')

    def __repr__(self):
        return f"Student_Table(student_id={self.student_id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"date_of_birth={self.date_of_birth}, gender={self.gender}, address={self.address}, " \
               f"guardian_name={self.guardian_name}, contact_number={self.contact_number}, class_id={self.class_id}, " \
               f"admission_date={self.admission_date})"