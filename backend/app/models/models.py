from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nif = db.Column(db.String(150), nullable=False)
    morada = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(150), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_number = db.Column(db.Intager(150), nullable=False)
    function = db.Column(db.String(150), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Oficina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(150), nullable=False)
    brand = db.Column(db.String(150), nullable=False)
    model = db.Column(db.String(150), nullable=False)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    id_oficina = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    id_car = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    
    
class ServiceStaff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Float, nullable=False)
    id_service = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    id_staff = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    id_oficina = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False) 
    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    
class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    total_price = db.Column(db.Float, nullable=False)
    id_service = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    id_service_staff = db.Column(db.Integer, db.ForeignKey('service_staff.id'), nullable=False)
    id_products = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    id_oficina = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)



    
            