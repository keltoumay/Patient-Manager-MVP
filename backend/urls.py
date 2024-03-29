from flask import Flask
from views import create_patient, get_all_patients

# Create Flask application
app = Flask(__name__)

# Define URL patterns
app.add_url_rule('/patients', 'create_patient', create_patient, methods=['POST'])
app.add_url_rule('/patients', 'get_all_patients', get_all_patients, methods=['GET'])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
