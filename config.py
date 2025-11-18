USER = 'db_user'  # <-- IMPORTANT: Change this
PASSWORD = 'your_password'  # <-- IMPORTANT: Change this
HOST = 'localhost'
DATABASE = 'bond_db'

# SQLAlchemy connection string
# This is constructed from the values above
DB_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/"
DB_URL_WITH_DB = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"