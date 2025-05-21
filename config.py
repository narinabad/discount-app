import os

SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")
PORT = int(os.environ.get("PORT", 8080))

SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}"
    f"@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

