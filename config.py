import os

SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")
PORT = int(os.environ.get("PORT", 8080))

SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{os.environ['MYSQLUSER']}:{os.environ['MYSQLPASSWORD']}"
    f"@{os.environ['MYSQLHOST']}:{os.environ['MYSQLPORT']}/{os.environ['MYSQLDATABASE']}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
