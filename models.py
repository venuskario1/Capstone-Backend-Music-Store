from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import db, ma
import os


#Create the classes for the Models

#Instruments class
class Instrument(db.Model):
    __tablename__="Instruments"

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(100))
    model = db.Column(db.String(100))
    price = db.Column(db.Float)
    color = db.Column(db.String(100))

    def __init__(self,kind,model,price,color):
        self.kind = kind
        self.model = model
        self.price = price
        self.color = color 



    def __repr__(self):
        return '<Instruments {}>'.format(self.kind)

#ma Marshallow instantiation - above code
class InstrumentSchema(ma.Schema):

    class Meta:
        fields = ('id','kind','model','price','color') #property of schema

#Init Schema
instrument_schema = InstrumentSchema(strict=True) #calling it True is to avoid warnings in console
instruments_schema = InstrumentSchema(many=True, strict=True)








#Customers class
class Customer(db.Model):
    __tablename__="Customers"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):  # Every customer needs to be initialized with these set parameters - id will auto-assign
        self.name = name
        self.email = email


#ma Marshallow instantiation - above code
class CustomerSchema(ma.Schema):

    class Meta:
        fields = ('id','name','email')

#Init Schema
customer_schema = CustomerSchema(strict=True) #calling it True is to avoid warnings in console
customers_schema = CustomerSchema(many=True,strict=True)








#Lessons class
class Lesson(db.Model):
    __tablename__="Lesson"

    id = db.Column(db.Integer, primary_key=True)
    type1 = db.Column(db.String(100))
    message = db.Column(db.String(250))

    def __init__(self,type1,message):
        self.type1 = type1
        self.message = message

#ma Marshallow instantiation - above code
class LessonSchema(ma.Schema):

    class Meta:
        fields = ('id','type1','message')

#Init Schema
lesson_schema = LessonSchema(strict=True) #calling it True is to avoid warnings in console
lessons_schema = LessonSchema(many=True,strict=True)




