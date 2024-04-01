from extension import db


class Teachers_Table(db.Model):
    __tablename__ = 'teachers_table'
    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.DECIMAL(10, 2), nullable=False)

    def __repr__(self):
        return f"Teachers_Table(teacher_id={self.teacher_id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"date_of_birth={self.date_of_birth}, gender={self.gender}, address={self.address}, " \
               f"contact_number={self.contact_number}, email={self.email}, salary={self.salary}, " \
               f"hire_date={self.hire_date})"

