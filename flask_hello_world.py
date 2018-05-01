from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World yay!'


app.run(debug=True)
