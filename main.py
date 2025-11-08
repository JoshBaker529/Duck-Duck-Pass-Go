from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Temporary website for Duck Duck Pass Go'

if __name__ == '__main__':
    app.run(debug=True)
