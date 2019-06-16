from flask import Flask, render_template, url_for, request
from flask_bcrypt import Bcrypt
from data import Statuses

app = Flask(__name__)

bcrypt = Bcrypt()
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
    # data = [v for v in Statuses if v["caseno"] == caseno][0]
    data = [v for v in Statuses if bcrypt.check_password_hash(v['crypt_caseno'], caseno)][0]
    return render_template('statusdetail.html', data=data)


@app.route('/status_check', methods=['GET', 'POST'])
def statusCheck():
    if request.method == 'POST':
        caseno = request.form['caseno']
        try:
            data = [v for v in Statuses if bcrypt.check_password_hash(v['crypt_caseno'], caseno)][0]
            return render_template('statusdetail.html', data=data)
        except IndexError:
            return "Nothing to display"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
