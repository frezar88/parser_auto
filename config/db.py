from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.environ.get('DATA_BASE_CONNECTION'), isolation_level="READ UNCOMMITTED")
meta = MetaData()
con = engine.connect()
