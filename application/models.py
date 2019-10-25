from . import db

class ToDo(db.Model):
    """Data model for tasks"""

    __tablename__ = 'todo_list'
    id = db.Column(db.Integer,
                   primary_key=True)
    task = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    due_date = db.Column(db.Date,
                         index=False,
                         unique=False,
                         nullable=False)
    task_status = db.Column(db.String(20),
                         index=False,
                         unique=False,
                         nullable=False)


    @staticmethod
    def from_dict(dict):
        return ToDo(id=dict.get('id'), task=dict['task'], due_date=dict['due_date'], task_status=dict['task_status'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'  : self.id,
           'task': self.task,
           'due_date': self.due_date,
           'task_status': self.task_status
       }

# REFERENCE CLASS
#
# class Book(db.Model):
#     """Data model for books"""
#
#     __tablename__ = 'books'
#     id = db.Column(db.Integer,
#                    primary_key=True)
#     name = db.Column(db.String(64),
#                          index=False,
#                          unique=True,
#                          nullable=False)
#
#
#     @staticmethod
#     def from_dict(dict):
#         return Book(id=dict.get('id'), name=dict['name'])
#
#     def to_dict(self):
#        """Return object data in easily serializable format"""
#        return {
#            'id'  : self.id,
#            'name': self.name,
#        }