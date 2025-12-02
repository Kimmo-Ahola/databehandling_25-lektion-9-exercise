from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mysql_url = "mysql+pymysql://user:user123@localhost:3306/delete_me_2"

engine = create_engine(url=mysql_url)

My_Session = sessionmaker(engine)