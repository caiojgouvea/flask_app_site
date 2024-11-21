from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


app.run(debug=True, host='0.0.0.0', port=5000)