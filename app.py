from flask import Flask

# Create the application instance
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World123!'



if __name__ == '__main__':
    app.run(debug=True)
