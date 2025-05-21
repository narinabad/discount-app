SECRET_KEY='hsudyf.,mjhuygsauhipoo//.,'
PORT=8080
MYSQL_CONFIG = "mysql+mysqlconnector://root:xEgLoIwXkUjNIIbUuSakgsOReHNfAUOG@mysql.railway.internal:3306/railway"

import os
SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@"
    f"{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

