from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startseite():
    return render_template('index.html')

@app.route('/sexulitäten')
def identitaeten():
    return render_template('sexualitaeten.html')

@app.route('/ueber')
def ueber_uns():
    return render_template('ueber.html')

@app.route('/geschlechtesidentitäten')
def geschlechtesidentitäten():
    return render_template('geschlechtesidentitäten.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)