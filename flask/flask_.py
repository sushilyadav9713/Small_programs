from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Define the route for the root URL ("/")
@app.route("/home")
@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Rurlocalhost:5000
if __name__ == "__main__":
    app.run(debug=True)
