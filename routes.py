from app import app,db,ma
from flask import Flask, request, jsonify
from models import Instrument,Customer,Lesson,instrument_schema,instruments_schema,customer_schema,customers_schema,lesson_schema,lessons_schema
# from models import db


# Create API route for creating instrument
@app.route('/instruments',methods=['POST'])
def add_instrument():
    kind = request.json['kind']
    model = request.json['model']
    price = request.json['price']
    color = request.json['color']

    #init instruments with info
    new_instrument = Instrument(kind,model,price,color)

    db.session.add(new_instrument)
    db.session.commit()

    return instrument_schema.jsonify(new_instrument)


# GET All Instruments
@app.route('/instruments',methods=["GET"])
def get_instruments():
    all_instruments = Instrument.query.all()
    result = instruments_schema.dump(all_instruments)
    return jsonify(result.data)


#GET Single Instrument
@app.route('/instruments<id>',methods=["GET"])
def get_instrument(id):
    instrument = Instrument.query.get(id)
    return instrument_schema.jsonify(instrument)


#Update an Instrument
@app.route('/instruments/<id>',methods=["PUT"])
def update_instrument(id):
    instrument = Instrument.query.get(id)

    kind = request.json['kind']
    model = request.json['model']
    price = request.json['price']
    color = request.json['color']

    instrument.kind = kind
    instrument.model = model
    instrument.price = price
    instrument.color = color

    db.session.commit()

    return instrument_schema.jsonify(instrument)


#Delete Instruments
@app.route('/instruments/<id>',methods=["DELETE"])
def delete_instruments(id):
    instrument = Instrument.query.get(id)
    db.session.delete(instrument)
    db.session.commit()

    return instrument_schema.jsonify(instrument)





#Create API Route for Customer 
@app.route('/customer',methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']

    #init cars with info
    new_customer = Customer(name,email)

    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)

#GET All Customers
@app.route('/customers',methods=["GET"])
def get_customers():
    all_customers = Customer.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result.data)


#GET Single Customer
@app.route('/customers/<id>',methods=["GET"])
def get_customer(id):
    customer = Customer.query.get(id)
    return customer_schema.jsonify(customer)

#Update a Customer
@app.route('/customers/<id>',methods=["PUT"])
def update_customer(id):
    customer = Customer.query.get(id)

    name = request.json['name']
    email = request.json['emal']

    customer.name = name
    customer.email = email

    db.session.commit()

    return customer_schema.jsonify(customer)

#Delete Customer
@app.route('/customer/<id>',methods=["DELETE"])
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()

    return customer_schema.jsonify(customer)






#Create API Route for Creating Lessons
@app.route('/lessons',methods=['POST'])
def add_lesson():
    type1 = request.json['type1']
    message = request.json['message']


    #initialize lessons with info
    new_lesson = Lesson(type1,message)


    db.session.add(new_lesson) #open the session
    db.session.commit()

    return lesson_schema.jsonify(new_lesson)

# Retrieve (GET) all lessons
@app.route('/lessons',methods=['GET'])
def get_lessons():
    all_lessons = Lesson.query.all()
    result = lessons_schema.dump(all_lessons)
    return jsonify(result.data)


# Retrieve (GET) single lesson
@app.route('/lessons',methods= ['GET'])
def get_lesson(id):
    lesson = Lesson.query.get(id)
    return lesson_schema.jsonify(lesson)


# Update a lesson (inside of our database)
@app.route('/lesson/<id>',methods=['PUT'])
def update_lesson(id):
    lesson = Lesson.query.get(id)

    type1 = request.json['type1']
    message = request.json['message']

    lesson.type1 = type1
    lesson.message = message

    db.session.commit()

    return lesson_schema.jsonify(lesson)

# Delete lesson
@app.route('/lessons/<id>',methods=['DELETE'])
def delete_lesson(id):
    lesson = Lesson.query.get(id)

    db.session.delete(lesson)
    db.session.commit()

    return lesson_schema.jsonify(lesson)

