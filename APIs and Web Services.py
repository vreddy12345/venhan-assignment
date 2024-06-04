11. REST API Basics 

Write a simple REST API using Flask with one endpoint /greet/<name> that returns a JSON  response with a greeting message, e.g., `{"message": "Hello, <name>!"}`.


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    message = f"Hello, {name}!"
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
