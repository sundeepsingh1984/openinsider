import sys,os,pathlib
from sqlalchemy.sql.expression import null

from sqlalchemy.sql.sqltypes import DATETIME

# we're appending the app directory to our path here so that we can import config easily
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,UniqueConstraint, ForeignKey, Sequence, Text, Boolean, Float, Enum, BigInteger,TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects import postgresql
import enum
from dictalchemy import DictableModel,make_class_dictable
Base= declarative_base()

make_class_dictable(Base)


class Insider(Base):
    __tablename__="insider"

    #primary key
    id=Column(String,primary_key=True,autoincrement=True)
    x=Column(String,nullable=True,default="na")
    filling_date=Column(DateTime,nullable=False)
    trade_date=Column(DateTime,nullable=False)
    insider_name=Column(String,nullable=False)
    title=Column(String,nullable=False)
    price=Column(Float,nullable=True)
    quantity=Column(BigInteger,nullable=False)
    owned=Column(BigInteger,nullable=False)
    own_percent=Column(Float,nullable=False)
    value=Column(BigInteger,nullable=True)
    day=Column(BigInteger,nullable=True)
    week=Column(BigInteger,nullable=True)
    month=Column(BigInteger,nullable=True)
    year_half=Column(BigInteger,nullable=True)






#enumerates for crons

class Ctype(enum.Enum):
    started=1
    failed=2
    completed=3



#table for crons

class Cron(Base):
    __tablename__="crons"    
    
    #primary key
    id=Column(Integer,primary_key=True,autoincrement=True)
    
    #columns
    cron_id=Column(String,nullable=False)
    cron_name=Column(String,nullable=False)
    cron_status=Column(Enum(Ctype))
    started_at=Column(DateTime(timezone=True),server_default=func.now())
    completed_at=Column(DateTime(timezone=True),server_default=func.now())


