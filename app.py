from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        req = request.form
        print(req)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)