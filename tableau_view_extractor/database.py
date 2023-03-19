"""Create database connection and session."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from . import r


engine = create_engine(r.get("uri"), convert_unicode=True, echo=False)
db_session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()
