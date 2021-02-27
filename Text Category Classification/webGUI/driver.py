from flask import Flask ,render_template,request,Response
from model import myinput
from os.path import join, dirname, realpath

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2', methods=['POST'])
def page2():
	text = request.form['text']
	predicted_result, prob_list = myinput(text)
	return render_template("page2.html",result=predicted_result)

if __name__ == '__main__':
    app.run(debug=True)