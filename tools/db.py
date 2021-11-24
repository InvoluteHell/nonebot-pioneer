from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

engine = create_engine(
    environ.get("db", "sqlite+pysqlite:///:memory:"),
    echo=True,
    future=True,
)
"""global engine for sqlalchemy"""

make_session = sessionmaker(engine)
"""Session maker for global engine"""

mapper_registry = registry()

Base = mapper_registry.generate_base()
"""Base model class for sqlalchemy"""
