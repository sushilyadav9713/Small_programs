from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define the route for the root URL ("/")
@app.route("/home")
@app.route("/")
def hello_world():
    return "Hello, World!"


# Run the Flask app on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
