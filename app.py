from flask import Flask, render_template
from flask import request, redirect
from predictor import wsi_magic

app = Flask(__name__)
it_text = ""
@app.route('/',methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        req = request.form
        it_text = wsi_magic(req['message'])
        print(it_text)
        return redirect('/result/'+it_text)

    return render_template('index.html')
@app.route('/result/<result>')
def result(result):
    return render_template('result.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)