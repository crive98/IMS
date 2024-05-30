from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/information')
def info():
    return '<h1> Here are some info! </h1>'

@app.route('/company/<name>')
def company(name):
    return '<h1> This is a page for {} </h1>'.format(name)

if __name__ == '__main__':
    app.run()