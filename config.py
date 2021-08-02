import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/pybo.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
