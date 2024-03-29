from flask import Flask

# Create Flask application
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return 'Welcome to the Patient Manager backend!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
