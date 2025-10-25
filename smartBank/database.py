from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
engine = create_engine('postgresql://postgres:hackathonHCL@db.wtnjjayobyhhswynbfce.supabase.co:5432/postgres',echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)