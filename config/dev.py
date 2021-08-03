SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='postgres',
    pw='mypybotest',
    url='postgresql',
    db='flask_pybo_dev')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
