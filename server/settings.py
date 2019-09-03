import os
SECRET_KEY = os.environ.get('SECRET_KEY') or 'testsecret'
TOKEN_EXPIRATION_SECONDS= 60*30
