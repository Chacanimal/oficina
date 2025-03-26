class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senha@localhost:3306/oficina_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key_example'  # Modifica com a chave secreta real
