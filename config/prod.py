SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='postgres',
    pw='mypybotest',
    url='postgresql',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'b\xf0\xe2\xc4\xe21rP(7\nX\xc9\xf1=\xbd3'
