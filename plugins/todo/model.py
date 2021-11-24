from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from tools.db import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
