from extension import db

class Classes_Table(db.Model):
    __tablename__ = 'classes_table'
    class_id = db.Column(db.Integer, primary_key=True, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    class_teacher_id = db.Column(db.Integer, db.ForeignKey('teachers_table.teacher_id'))

    def __repr__(self):
        return f"Classes_Table(class_id={self.class_id}, class_name={self.class_name}, class_teacher_id={self.class_teacher_id})"

