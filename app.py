from flask import Flask, render_template

app = Flask('teste')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ola')
def olaMundo():
    return "Olá mundo com FLASK"


app.run(debug=True)
