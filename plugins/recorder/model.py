from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from tools.db import Base


class MessageRecord(Base):
    __tablename__ = "message_record"
    type = Column(String)
