import databases
import sqlalchemy

from storeapi.config import config

meta = sqlalchemy.MetaData()

post_table = sqlalchemy.Table(
    "posts",
    meta,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "body",
        sqlalchemy.String,
    ),
)

comment_table = sqlalchemy.Table(
    "comments",
    meta,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False),
)

engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args={"check_same_thread": False}
)
meta.create_all(engine)

database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
