import flask
import spamCheck

app = flask.Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return flask.render_template('dashboard.html')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/check', methods=['POST'])
def checkText():
    if flask.request.method == 'POST':
        return spamCheck.checkSpam(flask.request.form)
    else:
        return


if __name__ == '__main__':
    app.debug = True
    app.run()
