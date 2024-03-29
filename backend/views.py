from flask import Flask, request, jsonify
from models import Patient, Session, engine

# Create Flask application
app = Flask(__name__)

# Create session
Session.configure(bind=engine)
session = Session()

# API endpoint to create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    
    # Create a new Patient object
    new_patient = Patient(
        first_name=data['first_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        phone_number=data['phone_number'],
        email=data['email'],
        address=data['address']
    )
    
    # Add the new patient to the database session
    session.add(new_patient)
    session.commit()
    
    return jsonify({'message': 'Patient created successfully'})

# API endpoint to retrieve all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    patients = session.query(Patient).all()
    patients_data = [{'id': patient.id, 'first_name': patient.first_name, 'last_name': patient.last_name} for patient in patients]
    return jsonify({'patients': patients_data})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
