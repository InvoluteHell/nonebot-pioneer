from sqlalchemy import create_engine
from os import environ
from sqlalchemy.orm import registry
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer

engine = create_engine(
    environ.get("db", "sqlite+pysqlite:///:memory:"), echo=True, future=True
)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
