from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)
it_text = ""
@app.route('/',methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        req = request.form
        it_text = req['message']
        return redirect('/result/'+it_text)

    return render_template('index.html')
@app.route('/result/<result>')
def result(result):
    return render_template('result.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)