import os 
from dotenv import load_dotenv


# ISTO CARREGA AS VARIAVEIS DE AMBIENTE DO FICHEIRO .env
load_dotenv()

class Config:
    SQ|ALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")