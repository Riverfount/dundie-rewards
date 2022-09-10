import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issue/189
from sqlmodel.sql.expression import Select, SelectOfScalar

from dundie import models  # Importante
from dundie.settings import SQL_CONN_STRING

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore

warnings.filterwarnings(
    'ignore', category=SAWarning
)

engine = create_engine(SQL_CONN_STRING, echo=False)
models.SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    return Session(engine)
