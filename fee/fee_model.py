from extension import db


class Fees_Table(db.Model):
    __tablename__ = 'fees_table'
    fee_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.student_id'))
    fee_amount = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    status = db.Column(db.String(10), nullable=False) 

    def __repr__(self):
        return f"Fees_Table(fee_id={self.fee_id}, student_id={self.student_id}, fee_amount={self.fee_amount}, amount={self.amount}, status={self.status})"        
