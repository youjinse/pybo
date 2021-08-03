SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='postgres',
    pw='mypybotest',
    url='127.0.0.1',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
