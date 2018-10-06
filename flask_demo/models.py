from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,String,Text,Date,DateTime
from sqlalchemy import create_engine


# 第二步：导入db，在表中加入db.M
from flask_demo import db
class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    # abc = Column(String(32), index=True, nullable=False)