from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def form():
	return render_template('form_submit.html')

@app.route('/hello', methods = ['POST'])
def hello():
	scenario = request.form['scenario']
	message = "Showing maps for scenario " + scenario + ":"
	return render_template('form_action.html', message=message)


if __name__ == '__main__':
   app.run(debug = True)