from flask import Flask, render_template, url_for, request
from data import Statuses

app = Flask(__name__)

Statuses = Statuses()


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/status')
def status():
    return render_template('status.html', statuses=Statuses)


@app.route('/status/<string:caseno>/')
def statusDetail(caseno):
    data = [v for v in Statuses if v["caseno"] == caseno][0]
    return render_template('statusdetail.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
